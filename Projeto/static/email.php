<?php
if (isset($_POST['BTEnvia'])) {
 
 //Variaveis de POST, Alterar somente se necessário 
 //====================================================
 $nome = $_POST['Nome'];
 $email = $_POST['emai'];
 $telefone = $_POST['telefone']; 
 $mensagem = $_POST['message'];
 //====================================================
 //<div class="content col-lg-4 col-sm-4 col-md-2 mt-4">
					//<div class="contato animat-up">

						//<form class="form">
							//<input class="field" name="Nome" placeholder="Nome">
							//<input class="field" name="emai" placeholder="Email">
							//<input class="field" name="telefone" placeholder="Telefone">
							//<textarea class="field" name="message" placeholder="Digite Sua mensagem Aqui"></textarea>

							//<input class="field" type="submit" value="Enviar">
						//</form>

					//</div>
				//</div>

 //REMETENTE --> ESTE EMAIL TEM QUE SER VALIDO DO DOMINIO
 //==================================================== 
 $email_remetente = "email@doseudominio"; // deve ser uma conta de email do seu dominio 
 //====================================================
 
 //Configurações do email, ajustar conforme necessidade
 //==================================================== 
 $email_destinatario = "douglasf.gama@gmail.com"; // pode ser qualquer email que receberá as mensagens
 $email_reply = "$email"; 
 $email_assunto = "Orçamento - Laje"; // Este será o assunto da mensagem
 //====================================================
 
 //Monta o Corpo da Mensagem
 //====================================================
 $email_conteudo = "Nome = $Nome \n"; 
 $email_conteudo .= "Email = $emai \n";
 $email_conteudo .= "Telefone = $telefone \n"; 
 $email_conteudo .= "Mensagem = $message \n"; 
 //====================================================
 
 //Seta os Headers (Alterar somente caso necessario) 
 //==================================================== 
 $email_headers = implode ( "\n",array ( "From: $email_remetente", "Reply-To: $email_reply", "Return-Path: $email_remetente","MIME-Version: 1.0","X-Priority: 3","Content-Type: text/html; charset=UTF-8" ) );
 //====================================================
 
 //Enviando o email 
 //==================================================== 
 if (mail ($email_destinatario, $email_assunto, nl2br($email_conteudo), $email_headers)){ 
 echo "</b>E-Mail enviado com sucesso!</b>"; 
 } 
 else{ 
 echo "</b>Falha no envio do E-Mail!</b>"; } 
 //====================================================
} 
?>
 