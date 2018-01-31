---
UID : NS:d3dkmddi._DXGK_SETVIDPNSOURCEADDRESS_FLAGS
title : "_DXGK_SETVIDPNSOURCEADDRESS_FLAGS"
author : windows-driver-content
description : The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's DxgkDdiSetVidPnSourceAddress or DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay functions.
old-location : display\dxgk_setvidpnsourceaddress_flags.htm
old-project : display
ms.assetid : cdc4aec6-45d4-4a5b-aa52-7830494a12b6
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : d3dkmddi/DXGK_SETVIDPNSOURCEADDRESS_FLAGS, DmStructs_45e34e9d-e410-44f4-a41a-aad748f01688.xml, DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure [Display Devices], _DXGK_SETVIDPNSOURCEADDRESS_FLAGS, DXGK_SETVIDPNSOURCEADDRESS_FLAGS, display.dxgk_setvidpnsourceaddress_flags
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows Vista.
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_SETVIDPNSOURCEADDRESS_FLAGS
---

# _DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure
The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> or <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay.md">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> functions.

## Syntax
````
typedef struct _DXGK_SETVIDPNSOURCEADDRESS_FLAGS {
  union {
    struct {
      UINT ModeChange  :1;
      UINT FlipImmediate  :1;
      UINT FlipOnNextVSync  :1;
      UINT FlipStereo  :1;
      UINT FlipStereoTemporaryMono  :1;
      UINT FlipStereoPreferRight  :1;
      UINT SharedPrimaryTransition  :1;
      UINT IndependentFlipExclusive  :1;
      UINT MoveFlip  :1;
      UINT Reserved  :23;
    };
    UINT Value;
  };
} DXGK_SETVIDPNSOURCEADDRESS_FLAGS;
````

## Members


## Remarks
If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:
<ul>
<li>The <b>hAllocation</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a> structure points to an allocation that is created with the <b>Stereo</b> member set in the <b>Flags</b> member of the <a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_displaymode.md">D3DKMT_DISPLAYMODE</a> structure.</li>
<li>The <b>PrimarySegment</b> and <b>PrimaryAddress</b> members of <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a> point to the starting physical address of the allocation.</li>
<li>The driver honors the settings of the <b>FlipImmediate</b> and <b>FlipOnNextVSync</b> members of  the <b>DXGK_SETVIDPNSOURCEADDRESS_FLAGS</b> structure.</li>
</ul>Beginning with Windows 8, the display miniport driver can fail a call to the <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> function, returning STATUS_INVALID_PARAMETER, when the <b>SharedPrimaryTransition</b> member is set in <i>pSetVidPnSourceAddress</i>-&gt;<b>Flags</b>. However, such a failure is not expected unless there is an error in either the user mode driver's implementation of the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_checkdirectflipsupport.md">CheckDirectFlipSupport</a> function or in the Desktop Window Manager (DWM). If such a failure occurs, the operating system will not seamlessly fail back to composition mode, and presentation will be incorrect.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_displaymode.md">D3DKMT_DISPLAYMODE</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags.md">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a>

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay.md">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a>

<a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>