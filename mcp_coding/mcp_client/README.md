streamablehttp_client(self._server_url)

Creates a transport for talking to the MCP server over HTTP streaming.

Returns a context manager that yields three things:

_read: function to read incoming messages.

_write: function to send messages.

_get_session_id: helper for session tracking.