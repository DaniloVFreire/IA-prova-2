def findDecision(obj): #obj[0]: HISTORIA DE CREDITO, obj[1]: DIVIDA, obj[2]: GARANTIA, obj[3]: RENDA
	# {"feature": "RENDA", "instances": 20, "metric_value": 0.4967, "depth": 1}
	if obj[3] == 'acima de $35k':
		# {"feature": "HISTORIA DE CREDITO", "instances": 9, "metric_value": 0.2222, "depth": 2}
		if obj[0] == 'desconhecida':
			# {"feature": "DIVIDA", "instances": 4, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'baixa':
				return 'baixo'
			elif obj[1] == 'alta':
				return 'alto'
			else: return 'alto'
		elif obj[0] == 'boa':
			return 'baixo'
		elif obj[0] == 'ruim':
			return 'moderado'
		else: return 'moderado'
	elif obj[3] == '$15 a $35k':
		# {"feature": "HISTORIA DE CREDITO", "instances": 6, "metric_value": 0.2222, "depth": 2}
		if obj[0] == 'desconhecida':
			# {"feature": "DIVIDA", "instances": 3, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'baixa':
				return 'moderado'
			elif obj[1] == 'alta':
				return 'alto'
			else: return 'alto'
		elif obj[0] == 'ruim':
			return 'alto'
		elif obj[0] == 'boa':
			return 'moderado'
		else: return 'moderado'
	elif obj[3] == '$0 a $15k':
		# {"feature": "GARANTIA", "instances": 5, "metric_value": 0.0, "depth": 2}
		if obj[2] == 'nenhuma':
			return 'alto'
		elif obj[2] == 'adequada':
			return 'moderado'
		else: return 'moderado'
	else: return 'alto'
