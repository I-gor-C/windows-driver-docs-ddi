---
UID: NS:d3dkmthk._D3DKMT_SETGAMMARAMP
title: "_D3DKMT_SETGAMMARAMP"
author: windows-driver-content
description: The D3DKMT_SETGAMMARAMP structure describes parameters for setting the gamma ramp.
old-location: display\d3dkmt_setgammaramp.htm
old-project: display
ms.assetid: aeab6bf1-bb6f-427e-a566-942b3fb061b2
ms.author: windowsdriverdev
ms.date: 4/16/2018
ms.keywords: D3DKMT_SETGAMMARAMP, D3DKMT_SETGAMMARAMP structure [Display Devices], OpenGL_Structs_3f9b4d19-5367-43bb-94a7-288d375412d7.xml, _D3DKMT_SETGAMMARAMP, d3dkmthk/D3DKMT_SETGAMMARAMP, display.d3dkmt_setgammaramp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmthk.h
api_name:
-	D3DKMT_SETGAMMARAMP
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_SETGAMMARAMP
---

# _D3DKMT_SETGAMMARAMP structure


## -description


The D3DKMT_SETGAMMARAMP structure describes parameters for setting the gamma ramp.


## -struct-fields




### -field hDevice

[in] A handle to the device.


### -field VidPnSourceId

[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology for the VidPN source. 


### -field Type

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544565">D3DDDI_GAMMARAMP_TYPE</a>-typed value. This member can be one of the following: D3DDDI_GAMMARAMP_UNINITIALIZED (0), D3DDDI_GAMMARAMP_DEFAULT (1), D3DDDI_GAMMARAMP_RGB256x3x16 (2), or D3DDDI_GAMMARAMP_DXGI_1 (3).


### -field pGammaRampRgb256x3x16

[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544571">D3DDDI_GAMMA_RAMP_RGB256x3x16</a> structure. The union that is contained in D3DKMT_SETGAMMARAMP holds a structure of this type if the <b>Type</b> member is D3DDDI_GAMMARAMP_RGB256x3x16.


### -field pGammaRampDXGI1

[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544568">D3DDDI_GAMMA_RAMP_DXGI_1</a> structure. The union that is contained in D3DKMT_SETGAMMARAMP holds a structure of this type if the <b>Type</b> member is D3DDDI_GAMMARAMP_DXGI_1.


### -field Size

[in] The size of the D3DDDI_GAMMA_RAMP_RGB256x3x16 or D3DDDI_GAMMA_RAMP_DXGI_1 structure that <a href="https://msdn.microsoft.com/library/windows/hardware/ff544571">D3DDDI_GAMMA_RAMP_RGB256x3x16</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544568">D3DDDI_GAMMA_RAMP_DXGI_1</a> points to.


## -see-also




<a href="https://msdn.microsoft.com/library/windows/hardware/ff544565">D3DDDI_GAMMARAMP_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544568">D3DDDI_GAMMA_RAMP_DXGI_1</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544571">D3DDDI_GAMMA_RAMP_RGB256x3x16</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547174">D3DKMTSetGammaRamp</a>
 

 

