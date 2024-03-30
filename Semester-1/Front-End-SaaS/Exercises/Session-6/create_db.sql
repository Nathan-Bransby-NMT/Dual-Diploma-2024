
CREATE DATABASE nb_saad_fed if NOT EXISTS;

CREATE USER 'nb_saas_fed@127.0.0.1' 
    IDENTIFIED BY 'Password1';

GRANT USAGE ON *.* TO  'nb_saas_fed@127.0.0.1';

GRANT ALL on `nb\_saas\_fed`.* 
    TO 'nb_saas_fed@127.0.0.1'
    WITH GRANT OPTION;

FLUSH PRIVILEGES;
