DROP TABLE IF EXISTS color_data;

CREATE TABLE color_data
(
  id serial NOT NULL,
  red integer NOT NULL,
  green integer NOT NULL,
  blue integer NOT NULL,
  entry_name character varying(50) NOT NULL,
  submission_time timestamp without time zone DEFAULT date_trunc('second', localtimestamp),
  color_guess character varying(30) NOT NULL,
  session_id text NOT NULL,
  CONSTRAINT pk_color_data PRIMARY KEY (id)
);