import uuid

from sqlparams import SQLParams


class DBAdapter2:

    def __init__(self, db_connection, control_transaction: bool = True):
        self._db = db_connection
        self._transaction = None
        self._control_transaction = control_transaction

    def begin(self):
        if self._transaction is None:
            self._transaction = self._db.begin()

    def commit(self):
        if self._transaction is not None:
            self._transaction.commit()
            self._transaction = None

    def rollback(self):
        if self._transaction is not None:
            self._transaction.rollback()
            self._transaction = None

    def in_transaction(self):
        return self._transaction is not None

    def execute(self, sql: str, **kwargs) -> int:
        """
        Executando uma instrução sql sem retorno.
        É obrigatório a passagem de uma conexão de banco no argumento self._db.

        Retorna o número de linhas afetadas pela instrução.
        """
        cur = None
        try:
            cur = self._execute(sql, **kwargs)

            return cur.rowcount
        finally:
            if cur is not None:
                cur.close()

    def execute_query_to_model(self, sql: str, model_class: object, **kwargs) -> list:
        """
        Executando uma instrução sql com retorno.
        O retorno é feito em forma de uma lista (list), com elementos do tipo passado pelo parâmetro
        "model_class".
        É importante destacar que para cada coluna do retorno, será procurado um atributo no model_class
        com mesmo nome, para setar o valor. Se este não for encontrado, a coluna do retorno é ignorada.
        """

        result = []
        cur = None
        try:
            cur = self._execute(sql, **kwargs)
            rs = cur.fetchall()

            for rec in rs:
                model = model_class()

                i = 0
                for column in cur.keys():
                    if (hasattr(model, column)):
                        setattr(model, column, rec[i])

                    i += 1

                result.append(model)

        finally:
            if cur is not None:
                cur.close()

        return result

    def execute_query(self, sql: str, **kwargs) -> list:
        """
        Executando uma instrução sql com retorno.
        O retorno é feito em forma de uma lista (list), com elementos do tipo dict (onde cada chave é igual ao
        nome do campo correspondente).
        """
        cur = None
        try:
            cur = self._execute(sql, **kwargs)
            rs = cur.fetchall()

            return [dict(rec.items()) for rec in rs]
        finally:
            if cur is not None:
                cur.close()

    def execute_query_first_result(self, sql: str, **kwargs) -> list:
        """
        Executando uma instrução sql com retorno.
        O retorno é feito em forma de um dict (onde cada chave é igual ao nome do campo correspondente).

        Apenas o primeiro registro é retornado (os demais serão descartados, se houverem).
        Caso não haja registros correspondentes a query, retorna None.
        """
        cur = None
        try:
            cur = self._execute(sql, **kwargs)
            rs = cur.fetchall()

            results = [dict(rec.items()) for rec in rs]

            if len(results) <= 0:
                return None
            else:
                return results[0]
        finally:
            if cur is not None:
                cur.close()

    def execute_query_first_result_to_model(self, sql: str, model_class: object, **kwargs) -> "model_class":
        """
        Executando uma instrução sql com retorno.
        O retorno é feito em forma de um objeto do tipo passado pelo parâmetro "model_class".
        É importante destacar que para cada coluna do retorno, será procurado um atributo no model_class
        com mesmo nome, para setar o valor. Se este não for encontrado, a coluna do retorno é ignorada.
        """

        result = None
        cur = None
        try:
            cur = self._execute(sql, **kwargs)
            rs = cur.fetchone()

            if (len(rs) > 0):
                model = model_class()

                i = 0
                for column in cur.keys():
                    if (hasattr(model, column)):
                        setattr(model, column, rs[i])

                    i += 1

                result = model

        finally:
            if cur is not None:
                cur.close()

        return result

    def get_single_result(self, sql: str, **kwargs):
        """
        Executa uma instrução SQL para a qual se espera um único retorno (com tipo primitivo). Exemplo:
        select 1+1
        Se não houver retorno, retorna None.
        """
        cur = None
        try:
            cur = self._execute(sql, **kwargs)
            return cur.scalar()
        finally:
            if cur is not None:
                cur.close()

    def _check_type(self, parameter):
        if (isinstance(parameter, uuid.UUID)):
            return str(parameter)
        else:
            return parameter

    def _execute(self, sql: str, **kwargs):

        new_transaction = not self.in_transaction()

        try:
            if self._control_transaction and new_transaction:
                self.begin()

            if (kwargs is not None):
                pars = {key: self._check_type(kwargs[key]) for key in kwargs}
                sql2, pars2 = SQLParams('named', 'format').format(sql, pars)
                return self._db.execute(sql2, pars2)
            else:
                return self._db.execute(sql)
        except:
            if self._control_transaction and new_transaction:
                self.rollback()
            raise

        finally:
            if self._control_transaction and new_transaction:
                self.commit()

    # def execute_query_from_file(self, query_file_path, *parameters):
    #     with open(query_file_path) as f:
    #         sql = f.read()
    #     return self.execute_query(sql, parameters)
