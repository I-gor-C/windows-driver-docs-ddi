---
UID: NS:d3dkmddi._DXGK_SETVIDPNSOURCEADDRESS_FLAGS
title: "_DXGK_SETVIDPNSOURCEADDRESS_FLAGS"
author: windows-driver-content
description: The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's DxgkDdiSetVidPnSourceAddress or DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay functions.
old-location: display\dxgk_setvidpnsourceaddress_flags.htm
old-project: display
ms.assetid: cdc4aec6-45d4-4a5b-aa52-7830494a12b6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_SETVIDPNSOURCEADDRESS_FLAGS, DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure [Display Devices], DmStructs_45e34e9d-e410-44f4-a41a-aad748f01688.xml, _DXGK_SETVIDPNSOURCEADDRESS_FLAGS, d3dkmddi/DXGK_SETVIDPNSOURCEADDRESS_FLAGS, display.dxgk_setvidpnsourceaddress_flags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_SETVIDPNSOURCEADDRESS_FLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_SETVIDPNSOURCEADDRESS_FLAGS
---

# _DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure
The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> or <a href="https://msdn.microsoft.com/95108e45-1a3a-4a75-8719-0caadb911469">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> functions.

## Syntax
```
typedef struct _DXGK_SETVIDPNSOURCEADDRESS_FLAGS {
  union {
    struct {
      UINT  : 1  ModeChange;
      UINT  : 1  FlipImmediate;
      UINT  : 1  FlipOnNextVSync;
      UINT  : 1  FlipStereo;
      UINT  : 1  FlipStereoTemporaryMono;
      UINT  : 1  FlipStereoPreferRight;
      UINT  : 1  SharedPrimaryTransition;
      UINT  : 1  IndependentFlipExclusive;
      UINT  : 1  MoveFlip;
#if ...
      UINT  : 23 Reserved;
#elif
      UINT  : 24 Reserved;
#elif
      UINT  : 25 Reserved;
#else
      UINT  : 29 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_SETVIDPNSOURCEADDRESS_FLAGS;
```

## Members


## Remarks
If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:

<ul>
<li>The <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a> structure points to an allocation that is created with the <b>Stereo</b> member set in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a> structure.</li>
<li>The <b>PrimarySegment</b> and <b>PrimaryAddress</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a> point to the starting physical address of the allocation.</li>
<li>The driver honors the settings of the <b>FlipImmediate</b> and <b>FlipOnNextVSync</b> members of  the <b>DXGK_SETVIDPNSOURCEADDRESS_FLAGS</b> structure.</li>
</ul>
Beginning with Windows 8, the display miniport driver can fail a call to the <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> function, returning STATUS_INVALID_PARAMETER, when the <b>SharedPrimaryTransition</b> member is set in <i>pSetVidPnSourceAddress</i>-&gt;<b>Flags</b>. However, such a failure is not expected unless there is an error in either the user mode driver's implementation of the <a href="https://msdn.microsoft.com/BB909041-0194-4828-ACA2-E3F6B1974DBB">CheckDirectFlipSupport</a> function or in the Desktop Window Manager (DWM). If such a failure occurs, the operating system will not seamlessly fail back to composition mode, and presentation will be incorrect.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>



<a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a>



<a href="https://msdn.microsoft.com/95108e45-1a3a-4a75-8719-0caadb911469">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a>