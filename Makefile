install:
	[ -f laserEmb/embed.py ] || \
		curl -s https://raw.githubusercontent.com/facebookresearch/LASER/master/source/embed.py | awk '{if(NR>30&&NR<37)print("#",$$0);else print $$0}' > laserEmb/embed.py
	[ -f laserEmb/93langs.fcodes ] || \
		wget -P laserEmb/ https://dl.fbaipublicfiles.com/laser/models/93langs.fcodes
	[ -f laserEmb/93langs.fvocab ] || \
		wget -P laserEmb/ https://dl.fbaipublicfiles.com/laser/models/93langs.fvocab
	[ -f laserEmb/bilstm.93langs.2018-12-26.pt ] || \
		wget -P laserEmb/ https://dl.fbaipublicfiles.com/laser/models/bilstm.93langs.2018-12-26.pt
	pip install .
	echo "Install fastBPE and its Python binding manually: https://github.com/glample/fastBPE"

clean:
	rm -f laserEmb/embed.py laserEmb/93langs.fcodes laserEmb/93langs.fvocab laserEmb/bilstm.93langs.2018-12-26.pt
