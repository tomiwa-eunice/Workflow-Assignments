# WPS Execute Operation

import requests

wpsServerUrl = "http://130.89.221.193:85/geoserver/ows?"

result = []

buurt = ['Binnenstad-Noord', 'Binnenstad-Zuid', 'Ulk en omgeving', 'Java en omgeving', 'Bornsestraat en omgeving Midden', 'Riet Noord', 'Arendsboer en omgeving Noord', 'Aalderinkshoek Noordwest', 'Nieuwland', 'Arendsboer en omgeving Zuid', 'Riet Zuid', 'Bornsestraat en omgeving Zuid', 'Verspreide huizen wijk 11', 'Leemslagen-Noord', 'Vriezenveenseweg en omgeving Haghoek Oost', 'Parkweg en omgeving', 'Vriezenveenseweg en omgeving Haghoek West', 'Verspreide huizen wijk 12', 'Ootmarsumsestraat en omgeving', 'Aalderinkshoek Zuidoost', 'Markgraven', 'Rumerslanden', 'Aalderinkshoek Zuidwest', 'Wester-Sluitersveldlanden', 'Dijkstraat en omgeving', 'Rohof en omgeving', 'Kerkelanden', 'Verspreide huizen Nutter', 'Achterlanden en omgeving', 'Boomplaats', 'Ossenkoppelerhoek-Oost', 'Beeklust', 'Huttenveld', 'Verspreide huizen wijk 13', 'Aalderinkshoek Noordoost', 'Cromhoffsbleek-Kotman', 'Verspreide huizen wijk 14', 'Nieuwstraat en omgeving', 'Wonde en omgeving', 'Witvoet en omgeving', 'Ossenkoppelerhoek-Midden-Noord', 'Leemslagen-Zuid', 'Ossenkoppelerhoek-West', 'Ossenkoppelerhoek-Midden-Zuid', 'Hofkamp-West', 'Hofkamp-Oost', 'Paradijs', 'Schelfhorst-Noordwest', 'Havezathe', 'Kollenveld-Bolkshoek', 'Verspreide huizen Hofkamp', 'Schelfhorst-Zuidwest', 'Drakensteyn en omgeving', 'Schelfhorst-Noordoost', 'Schelfhorst-Zuidoost', 'Veenelanden', 'Groeneveld', 'Kanaalzijde', 'Zeven Bosjes', 'Leemslagen-Oost', 'Maardijk', 'De Grens', 'Nijrees', 'Verspreide huizen wijk 19', 'Aadorp-West', 'Aadorp-Oost', 'Bedrijvenpark Twente', 'Borne Centrum', "'t Wensink Noord", "'t Wensink Zuid", 'Verspreide huizen wijk 20', 'Bornerbroek', 'Verspreide huizen wijk 21', 'Boswinkel-De Braker', 'Bornsche Maten', 'Dikkerslaan-Molenkampsweg en omgeving', 'Lettersveld I', 'Lettersveld II', 'Tichelkamp', 'Stroom-Esch', 'De Bothoven', 'Hogeland-Noord', 'Getfert', 'Sleutelkamp', 'Verspreide huizen Borne-West', 'Veldkamp-Getfert-West', 'Hogeland-Zuid', 'Pathmos', 'Verspreide huizen Borne-Oost', 'Zenderen', 'Horstlanden-Stadsweide', 'Boddenkamp', 'Velve-Lindenhof', 'Stevenfenne', 'Wesselerbrink Noord-Oost', 'Verspreide huizen Zenderen', 'Hertme', 'Wooldrik', 'Varvik-Diekman', 'Stadsveld-Zuid', 'Verspreide huizen Hertme', 'City', 'Lasonder, Zeggelt', 'De Laares', "'t Weldink", 'De Leuriks', 'Elferink-Heuwkamp', 'Stadsveld-Noord-Bruggert', "'t Zwering", 'Ruwenbos', 'Tubantia-Toekomst', 'Twekkelerveld', 'Walhof-Roessingh', 'Bolhaar', 'Roombeek-Roomveldje', 'Mekkelholt', 'Stroinkslanden Noord-West', 'Deppenbroek', 'Voortman-Amelink', 'Drienerveld-U.T.', 'Schreurserve', 'Ribbelt-Ribbelerbrink', 'Park Stokhorst', 'Stokhorst', 'Veldmaat 2', 'Stroinkslanden Noord-Oost', 'Stroinkslanden-Zuid', 'Wesselerbrink Zuid-Oost', 'Wesselerbrink Zuid-West', 'Wesselerbrink Noord-West', 'Helmerhoek-Noord', 'Verspreide huizen Oud Ootmarsum', 'Helmerhoek-Zuid', 'het Brunink', 'Industrie- en havengebied', 'Marssteden', 'Koekoeksbeekhoek', 'De Broeierd', 'Glanerveld', 'Bentveld-Bultserve', 'Schipholt-Glanermaten', 'Eekmaat', 'Oikos', 'Eilermarke', 'De Slank', 'Dolphia', 'Eekmaat West', 'Dorp Lonneker', 'Dorp Boekelo', 'Noord Esmarke', 'De Pas', 'Buurtschap Lonneker-West', 'Buurtschap Zuid-Esmarke', 'Buurtschap Broekheurne', 'Buurtschap Usselo', 'Boekelerveld', 'De Els', 'Buurtschap Twekkelo', 'Haaksbergen Kern-1', 'Haaksbergen Kern-2', 'Haaksbergen Kern-3', 'Haaksbergen Kern-4', 'Veldmaat 1', 'Leemdijk', 'Zienesch', 'Wolferink 1 en 4', 'Wolferink 2', 'Wolferink 5', 'Wolferink 3', 'Hassinkbrink', 'Industriegebied West', 'Industriegebied Brammelo', 'Verspreide huizen Langelo ten noorden van de spoorlijn', 'Sint Isidorushoeve kern', 'Boeldershoek', 'Verspreide huizen Langelo (gedeeltelijk) en Honesch', 'Verspreide huizen Veldmaat ten zuiden van de spoorlijn', 'Verspreide huizen Veldmaat ten noorden van de spoorlijn', 'Verspreide huizen Sint Isidorushoeve', 'Buurse kern', 'Haaksbergen Kern-Centrum', 'Verspreide huizen Vroomshoop-Oost', 'Bedrijventerrein Zeggershoek', 'Verspreide huizen Bretelerveld', 'Bungalow-wijk', 'Verspreide huizen Buurse', 'Verspreide huizen Brammelo', 'Gijmink', 'Verspreide huizen Stepelo (gedeeltelijk)', 'Binnenstad-Centrum', 'Waterhoek', 'De inslag-De Kleies', 'Binnenstad-West', 'Glinde-Hooiland', 'Bedrijventerrein Timmersveld', 'Noord', 'Jufferbeek', 'Binnenstad-Oost', 'Hengelose Es-Noord', 'Tichelwerk', "'t Wilbert", 'Bovenhoek', 'Schothorsthoek', 'Elsbeek', 'De Meijbree', 'De Noork', 'Klein Driene', "'t Rot", 'Enter-West', 'Industriegebied Spechthorst I', 'Bartelinkshoek', 'Tijertshoek', 'Bruninkshoek', 'Middelhoek', 'Sogtoenhoek', 'Oosteinde en Slot', 'De Meene', 'Molendijkhoek', 'Westeinde', 'West ten oosten Kanaal', 'Industriegebied Kevelhammerhoek', 'Weijinkshoek', 'Groot Driene-Zuid', 'Oosterveld', 'Zwavertshoek', 'Anninks-/Nijhofshoek', 'Bedrijventerrein Twentekanaal-Noord II', 'Groot Driene-Noord', 'Bedrijventerrein Twentekanaal-Zuid II', 'Diepenheim-Zuid', 'Berflo Es Noord', 'West ten westen Kanaal', 'Berflo Es Zuid', 'Westerweilanden-Elzenhoek', 'Toekomstig bestemmingsplan Noord', 'De Whee II-Noord', 'Veldwijk-Noord', 'Veldwijk-Zuid', 'Industrieterrein Vriezenveen-West', 'Bedrijventerrein Twentekanaal-Zuid I', 'Bedrijventerrein Twentekanaal-Noord I', "Tuindorp 't Lansink", 'Nijverheid', 'Heeckeren', 'Tuindorp-Zuid', 'Vikkerhoek', 'Verspreide huizen De Westerhoeve', 'Verspreide huizen Markvelde', 'Bedrijventerrein Westermaat-Zuidwest', 'De Essen', 'Woolde', 'De Whee II-Zuid', 'Woolder Es', 'Verspreide huizen Tubbergen', 'Albergen kern', 'Weidedorp', 'Mariaparochie', 'Bedrijvenpark Westermaat-Zuidoost', 'Bedrijventerrein Westermaat-Noordoost', 'Dr. Schaepmanbuurt', 'Bedrijventerrein Westermaat-Noordwest', 'Beckum kern', 'Roershoek', 'Verspreide huizen ten noorden van Vriezenveen', 'Vossenbelt-Zuid', 'Verspreide huizen Mander', 'Reutum kern', 'Vossenbelt-Noord', 'Verspreide huizen Haarle', 'Westerhaar-West', 'Het Broek', 'Kristenbos', 'Dalmeden', 'Wierden-Noord', 'Wierden-West', 'Verspreide huizen Slangenbeek', 'De Maaten', 'Stadspark Weusthag-Noord', 'Verspreide huizen Twekkelo', 'Stadspark Weusthag-Zuid', 'Overdinkel kern', 'Verspreide huizen Driene', 'Verspreide huizen Overdinkel', 'Wierden-Oost', 'Verspreide huizen Oele', 'De Stouwe', 'Verspreide huizen Woolde', 'Verspreide huizen Beckum', 'Losser-West', "'t Loo", 'Broekmaten', 'Bedrijfsterrein Losser', 'Losser-Oost', 'Verspreide huizen Losser', 'Beuningen kern', 'Buurtschap Meer', 'Glane kern', 'Glane-beekhoek', 'Verspreide huizen Glane', 'Verspreide huizen Beuningen', 'Binnenstad Oldenzaal', 'De Lutte kern', 'Verspreide huizen De Lutte', 'De Hooilanden', 'Zuidbroek', 'Haerbroek-Scholtenhoek', 'Zuid-Bergenhuizen', 'Hanzepoort', 'Eekte-Hazewinkel', 'Verspreide huizen Huurne I', 'Het Hulsbeek', 'Verspreide huizen Huurne II', 'Westerhaar-Oost', 'De Thij', 'De Graven Es', 'Bekspring', 'Tubbergen-Dorp', 'Verspreide huizen Manderveen', 'Geerdijk-West', 'Verspreide huizen Albergen', 'Harbrinkhoek kern', 'Geerdijk-Oost', 'Verspreide huizen Harbrinkhoek', 'Geesteren kern', 'Verspreide huizen Geesteren', 'Langeveen kern', 'Verspreide huizen Langeveen', 'Vasse kern', 'Verspreide huizen Wierdenseveld', 'Verspreide huizen Hezingen', 'Verspreide huizen Vasse', 'Hooge-Hexel kern', 'Verspreide huizen Reutum', 'Fleringen kern', 'Verspreide huizen Fleringen', 'Wierden-Centrum', 'Verspreide huizen Lage Egge en omgeving', 'Verspreide huizen Broeklanden', 'Verspreide huizen Hooge-Hexel', 'Enter-Zuidwest', 'Enter-Noordwest', 'Enter-Oost', 'Industrieterrein', 'Verspreide huizen IJpelo', 'Verspreide huizen Waterhoek', 'Centrum-Goor', 'Verspreide huizen Enterveen en Elsslagen', 'Verspreide huizen Zuiderveld', 'Verspreide huizen Westerhaar-Vriezenveensewijk-West', 'Verspreide huizen Enterbroek en omgeving', 'Verspreide huizen Rectum', 'Verspreide huizen Notter', 'Industriegebied Spechthorst II', 'Verspreide huizen Zuna', 'Centrum-Vriezenveen', 'Midden', 'Verspreide huizen De Pollen', 'Verspreide huizen Weitemanslanden', 'Den Ham', "'t Sumpel", 'Verspreide huizen ten zuiden van Vriezenveen', 'Vriezenveensewijk', 'Verspreide huizen Westerhaar-Vriezenveensewijk-Oost', 'Buurtschap Magele', 'Buurtschap Linde', 'Vroomshoop-Oost', 'De Whee I', 'Vroomshoop-West', 'Beter Wonen', 'Nieuwoord', 'Kerspel', 'Markelo', 'Verspreide huizen Herike', 'Greekerinckskamp', "'t Kip", 'Verspreide huizen Markelerbroek', 'Schoppenstee', 'Verspreide huizen Stokkum', 'Vogelweiden', 'Verspreide huizen Markelo', 'Verspreide huizen Kerspel en Goor', 'Verspreide huizen Elzenerveen en Borkeld', 'Hooijerinkses', 'Verspreide huizen Elsen', 'Verspreide huizen Elsenerbroek', 'Diepenheim-Noord', 'Sint Annabrink', 'Verspreide huizen Kerspel en Schipbeek', 'Delden-Centrum', 'Oud Zuiderhagen', 'Rupertserf', 'Noord Deurningen kern', 'Vossenbrink en De Braak', 'Industrieterrein-Delden', 'Verspreide huizen Deldeneresch', 'Hengevelde', 'Verspreide huizen Noord Deurningen', 'Verspreide huizen Hengevelde', 'Verspreide huizen Deldenerbroek', "'t Stift", 'Verspreide huizen Deldeneresch', 'Verspreide huizen Wiene', 'Verspreide huizen Azelo', 'Verspreide huizen Zeldam', 'Bentelo kern', 'Verspreide huizen Bentelo', 'Centrum', 'Sombeek', 'Kerkeres', 'Buitengebied Denekamp', 'Lattrop kern', 'Klokkenberg', 'Dorper-Es', 'Tilligte kern', 'Veldkamp en Borchert', 'Janskamp', 'Diepengoor', "'t Pierik", 'Kloppendijk', 'Verspreide huizen Tilligte', 'Weerselo', 'Verspreide huizen Breklenkamp', 'Verspreide huizen Lattrop', 'Verspreide huizen Klein Agelo', 'Verspreide huizen Groot Agelo', 'Ootmarsum Kern', 'Ootmarsum Randkern', 'Wildehof', 'Ootmarsum villapark Stobbenkamp', 'Vinke-Brookhuis', 'Ootmarsum Cellenkamp Palthenkamp', 'Moerbekkenkamp', 'De Mors', 'Verspreide huizen Ootmarsum-Oost', 'Buitengebied Ootmarsum-West', 'Eertman', 'Reestman', "'t Spikkert", 'Echelpoel', 'Verspreide huizen Weerselo', 'Kern Deurningen', 'Rossum', 'Verspreide huizen Rossum', 'Saasveld', 'Verspreide huizen Saasveld', 'Verspreide huizen Deurningen']


for buur_name in buurt[0:5]:
	bu_name = buur_name.replace(' ', '+')
	payload = '''
		<wps:Execute version="1.0.0" service="WPS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.opengis.net/wps/1.0.0" xmlns:wfs="http://www.opengis.net/wfs" xmlns:wps="http://www.opengis.net/wps/1.0.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:wcs="http://www.opengis.net/wcs/1.1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/wps/1.0.0 http://schemas.opengis.net/wps/1.0.0/wpsAll.xsd">
		  <ows:Identifier>gs:Length</ows:Identifier>
		   <wps:DataInputs>
			<wps:Input>
			  <ows:Identifier>feature</ows:Identifier>
			  <wps:Reference mimeType="text/xml" xlink:href="http://geoserver/wps" method="POST">
				<wps:Body>
				  <wps:Execute version="1.0.0" service="WPS">
						 <ows:Identifier>gs:IntersectionFeatureCollection</ows:Identifier>
					<wps:DataInputs>
					  <wps:Input>
						<ows:Identifier>first feature collection</ows:Identifier>
						<wps:Reference mimeType="text/xml" xlink:href="http://geoserver/wps" method="POST">
						  <wps:Body>
							<wps:Execute version="1.0.0" service="WPS">
								   <ows:Identifier>gs:BufferFeatureCollection</ows:Identifier>
							  <wps:DataInputs>
								<wps:Input>
								  <ows:Identifier>features</ows:Identifier>
								  <wps:Reference mimeType="text/xml" xlink:href="http://geoserver/wps" method="POST">
									<wps:Body>
									  <wps:Execute version="1.0.0" service="WPS">
											 <ows:Identifier>gs:Centroid</ows:Identifier>
										<wps:DataInputs>
										  <wps:Input>
											<ows:Identifier>features</ows:Identifier>
											<wps:Reference mimeType="application/json" xlink:href="https://gisedu.itc.utwente.nl/cgi-bin/mapserv.exe?map=d:/iishome/exercise/data/afrialiance/layers.map&amp;version=2.0.0&amp;service=WFS&amp;request=GetFeature&amp;typeName=neighbourhood&amp;outputFormat=geojson&amp;srsname=EPSG:28992&amp;buname=%s" method="GET"/>
										  </wps:Input>
										</wps:DataInputs>
										<wps:ResponseForm>
										  <wps:RawDataOutput mimeType="application/json">
											<ows:Identifier>result</ows:Identifier>
										  </wps:RawDataOutput>
										</wps:ResponseForm>
									  </wps:Execute>
									</wps:Body>
								  </wps:Reference>
								</wps:Input>
								<wps:Input>
								  <ows:Identifier>distance</ows:Identifier>
								  <wps:Data>
									<wps:LiteralData>1000</wps:LiteralData>
								  </wps:Data>
								</wps:Input>
							  </wps:DataInputs>
							  <wps:ResponseForm>
								<wps:RawDataOutput mimeType="application/json">
								  <ows:Identifier>result</ows:Identifier>
								</wps:RawDataOutput>
							  </wps:ResponseForm>
							</wps:Execute>
						  </wps:Body>
						</wps:Reference>
					  </wps:Input>
					  <wps:Input>
						<ows:Identifier>second feature collection</ows:Identifier>
						<wps:Reference mimeType="application/json" xlink:href="https://gisedu.itc.utwente.nl/cgi-bin/mapserv.exe?map=d:/iishome/exercise/data/afrialiance/layers.map&amp;version=2.0.0&amp;service=WFS&amp;request=GetFeature&amp;typeName=streets&amp;outputFormat=geojson&amp;srsname=EPSG:28992" method="GET"/>
					  </wps:Input>
					</wps:DataInputs>
					<wps:ResponseForm>
					  <wps:RawDataOutput mimeType="application/json">
						<ows:Identifier>result</ows:Identifier>
					  </wps:RawDataOutput>
					</wps:ResponseForm>
				  </wps:Execute>
				</wps:Body>
			  </wps:Reference>
			</wps:Input>
		  </wps:DataInputs>
		  <wps:ResponseForm>
			<wps:RawDataOutput>
			  <ows:Identifier>result</ows:Identifier>
			</wps:RawDataOutput>
		  </wps:ResponseForm>
		</wps:Execute>'''%(bu_name)


	response = requests.post(wpsServerUrl, data=payload)
	length = response.text
	result.append({'neighbourhood': buur_name, 'length': length})

print("Content-type: application/json")
print()
print(result)
