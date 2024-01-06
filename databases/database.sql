BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS productos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
	codigo INTEGER,
    nombre TEXT,
    cantidad INTEGER,
    lote TEXT,
    fecha_vencimiento TEXT,
    destino TEXT,
    distribuidor TEXT,
    producto_disponible TEXT
);
INSERT INTO "productos" ("ID","codigo","nombre","cantidad","lote","fecha_vencimiento","destino","distribuidor","producto_disponible") VALUES (1,1160216,'Acetaminofen',5000,'12345','120523','c/s don bosco','Ramos','5000');
COMMIT;
