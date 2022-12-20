import file_to_uppercase

def test_output(capfd, monkeypatch):
    input = ['mbox-short.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    file_to_uppercase.print_file_as_uppercase()
    out, err = capfd.readouterr()
    assert "FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008" in out
    
