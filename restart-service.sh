supervisorctl -c supervisor.conf stop CrediteScitech
supervisorctl -c supervisor.conf reload
supervisorctl -c supervisor.conf start CrediteScitech
supervisorctl -c supervisor.conf status
