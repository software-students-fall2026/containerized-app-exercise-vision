"""Tests for the machine learning client."""

from client import main


def test_client_starts(capsys):
    """Check that the client starts successfully."""
    main()

    captured = capsys.readouterr()
    assert "Simon Says ML client is ready." in captured.out
