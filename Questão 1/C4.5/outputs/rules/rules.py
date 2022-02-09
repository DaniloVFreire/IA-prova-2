def findDecision(obj): #obj[0]: HISTORIA DE CREDITO, obj[1]: DIVIDA, obj[2]: GARANTIA, obj[3]: RENDA
	# {"feature": "GARANTIA", "instances": 20, "metric_value": 1.5395, "depth": 1}
	if obj[2] == 'nenhuma':
		# {"feature": "RENDA", "instances": 15, "metric_value": 1.371, "depth": 2}
		if obj[3] == '$15 a $35k':
			# {"feature": "DIVIDA", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'alta':
				# {"feature": "HISTORIA DE CREDITO", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0] == 'ruim':
					return 'alto'
				elif obj[0] == 'desconhecida':
					return 'alto'
				elif obj[0] == 'boa':
					return 'moderado'
				else: return 'moderado'
			elif obj[1] == 'baixa':
				return 'moderado'
			else: return 'moderado'
		elif obj[3] == 'acima de $35k':
			# {"feature": "HISTORIA DE CREDITO", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0] == 'boa':
				# {"feature": "DIVIDA", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1] == 'baixa':
					return 'baixo'
				elif obj[1] == 'alta':
					return 'baixo'
				else: return 'baixo'
			elif obj[0] == 'desconhecida':
				# {"feature": "DIVIDA", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'baixa':
					return 'baixo'
				elif obj[1] == 'alta':
					return 'alto'
				else: return 'alto'
			else: return 'baixo'
		elif obj[3] == '$0 a $15k':
			return 'alto'
		else: return 'alto'
	elif obj[2] == 'adequada':
		# {"feature": "HISTORIA DE CREDITO", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[0] == 'ruim':
			return 'moderado'
		elif obj[0] == 'boa':
			# {"feature": "RENDA", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3] == 'acima de $35k':
				return 'baixo'
			elif obj[3] == '$0 a $15k':
				return 'moderado'
			else: return 'moderado'
		elif obj[0] == 'desconhecida':
			return 'baixo'
		else: return 'baixo'
	else: return 'moderado'
