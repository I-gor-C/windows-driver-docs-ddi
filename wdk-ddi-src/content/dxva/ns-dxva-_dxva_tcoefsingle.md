---
UID : NS:dxva._DXVA_TCoefSingle
title : _DXVA_TCoefSingle
author : windows-driver-content
description : The DXVA_TCoefSingle structure is sent by the host decoder to the accelerator to specify IDCT coefficient values.
old-location : display\dxva_tcoefsingle.htm
old-project : display
ms.assetid : 665a9819-d319-414d-9a31-ee565b293197
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : dxva/DXVA_TCoefSingle, _DXVA_TCoefSingle, dxvaref_2b92ced3-3856-466f-b95a-84dd78426a0e.xml, LPDXVA_TCoefSingle, dxva/LPDXVA_TCoefSingle, DXVA_TCoefSingle, LPDXVA_TCoefSingle structure pointer [Display Devices], display.dxva_tcoefsingle, *LPDXVA_TCoefSingle, DXVA_TCoefSingle structure [Display Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dxva.h
req.include-header : Dxva.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXVA_TCoefSingle, *LPDXVA_TCoefSingle
---

# _DXVA_TCoefSingle structure
The DXVA_TCoefSingle structure is sent by the host decoder to the accelerator to specify <a href="https://msdn.microsoft.com/5a140cc0-ecc5-46ff-be3f-3c92f0f67dca">IDCT</a> coefficient values.

## Syntax
````
typedef struct _DXVA_TCoefSingle {
  WORD  wIndexWithEOB;
  SHORT TCoefValue;
} DXVA_TCoefSingle, *LPDXVA_TCoefSingle;
````

## Members


`TCoefValue`

Indicates the value of the coefficient in the block. <b>TCoefValue</b> must be clipped to the appropriate range as specified in <a href="https://msdn.microsoft.com/7736a226-1122-4380-b09f-a8560c0cd609">Low-Level IDCT Processing Elements</a> by the host prior to passing the coefficient value to the accelerator for <a href="https://msdn.microsoft.com/5a140cc0-ecc5-46ff-be3f-3c92f0f67dca">IDCT</a> operation. MPEG-2 mismatch control, if necessary, is also the responsibility of the host, not the accelerator. (This might require the creation of extra "phantom" nonzero coefficients.)

`wIndexWithEOB`

This member contains two fields: <i>TCoefIDX </i>and <i>TCoefEOB</i>.

## Remarks
The DXVA_TCoefSingle structure is used whenever the <i>HostResidDiff</i> flag (bit 10 in the <b>wMBtype</b> member of the <a href="..\dxva\ns-dxva-_dxva_mbctrl_p_offhostidct_1.md">DXVA_MBctrl_P_OffHostIDCT_1</a> or <a href="..\dxva\ns-dxva-_dxva_mbctrl_i_offhostidct_1.md">DXVA_MBctrl_I_OffHostIDCT_1</a> structure) is 1 and the <b>bConfig4GroupedCoefs</b> member of the <a href="..\dxva\ns-dxva-_dxva_configpicturedecode.md">DXVA_ConfigPictureDecode</a> structure is zero.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dxva.h (include Dxva.h) |

## See Also

<a href="..\dxva\ns-dxva-_dxva_configpicturedecode.md">DXVA_ConfigPictureDecode</a>

<a href="..\dxva\ns-dxva-_dxva_mbctrl_i_offhostidct_1.md">DXVA_MBctrl_I_OffHostIDCT_1</a>

<a href="..\dxva\ns-dxva-_dxva_mbctrl_p_offhostidct_1.md">DXVA_MBctrl_P_OffHostIDCT_1</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_TCoefSingle structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>