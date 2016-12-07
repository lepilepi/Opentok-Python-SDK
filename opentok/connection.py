class Connection(object):
    """
    Represents an OpenTok connection.

    Construct with a Session object and a connection ID

    Use the OpenTok.create_session() method to create an OpenTok session, or
    just invoke its constructor with the proper sdk and session_id.

    :ivar Session session: The Session of the connection.
    :ivar String connection_id: The connection ID.
    """
    def __init__(self, session, connection_id, **kwargs):
        self.session = session
        self.sdk = session.sdk
        self.connection_id = connection_id
        for key, value in kwargs.items():
            setattr(self, key, value)

    def force_disconnect(self):
        """
        Forces a client endpoint to disconnect from a session
        """
        self.sdk.force_disconnect_connection(self.session.session_id, self.connection_id)
