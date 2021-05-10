import { GUI } from '../../assets/three/jsm/libs/dat.gui.module';

export function CreatePanel() {

    var panel = new GUI( { width: 310 } );

    var folder1 = panel.addFolder( 'Visibility' );
    var folder2 = panel.addFolder( 'Activation/Deactivation' );
    var folder3 = panel.addFolder( 'Pausing/Stepping' );
    var folder4 = panel.addFolder( 'Crossfading' );
    var folder5 = panel.addFolder( 'Blend Weights' );
    var folder6 = panel.addFolder( 'General Speed' );
}