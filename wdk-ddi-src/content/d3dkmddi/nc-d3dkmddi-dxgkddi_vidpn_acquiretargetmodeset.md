---
UID : NC:d3dkmddi.DXGKDDI_VIDPN_ACQUIRETARGETMODESET
title : DXGKDDI_VIDPN_ACQUIRETARGETMODESET
author : windows-driver-content
description : The pfnAcquireTargetModeSet function returns a handle to a particular target mode set object that is contained by a specified VidPN object.
old-location : display\dxgk_vidpn_interface_pfnacquiretargetmodeset.htm
old-project : display
ms.assetid : 1b91c472-21eb-4aa8-91e3-c9eb70556d9f
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnAcquireTargetModeSet
req.alt-loc : d3dkmddi.h
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
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_VIDPN_ACQUIRETARGETMODESET callback function
The <b>pfnAcquireTargetModeSet</b> function returns a handle to a particular target mode set object that is contained by a specified VidPN object.

## Syntax

```
DXGKDDI_VIDPN_ACQUIRETARGETMODESET DxgkddiVidpnAcquiretargetmodeset;

NTSTATUS DxgkddiVidpnAcquiretargetmodeset(
  IN_CONST_D3DKMDT_HVIDPN hVidPn,
  IN_CONST_D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId,
  OUT_PD3DKMDT_HVIDPNTARGETMODESET phVidPnTargetModeSet,
  DEREF_OUT_CONST_PPDXGK_VIDPNTARGETMODESET_INTERFACE ppVidPnTargetModeSetInterface
)
{...}
```

## Parameters

`hVidPn`



`VidPnTargetId`

[in] An integer that identifies one of the video present targets associated with the VidPN object.

`phVidPnTargetModeSet`

[out] A pointer to a variable that receives a handle to the requested target mode set object.

`ppVidPnTargetModeSetInterface`

[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_vidpntargetmodeset_interface.md">DXGK_VIDPNTARGETMODESET_INTERFACE</a> structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the target mode set object.


## Return Value

The <b>pfnAcquireTargetModeSet</b> function returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function succeeded.
<dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN</b></dt>
</dl>The handle supplied in <i>hVidPn</i> was invalid.
<dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET</b></dt>
</dl>The identifier supplied in <i>VidPnTargetId</i> was invalid.

## Remarks

VidPN target identifiers are assigned by the display miniport driver. <a href="..\dispmprt\nc-dispmprt-dxgkddi_query_child_relations.md">DxgkDdiQueryChildRelations</a>, implemented by the display miniport driver, returns an array of <a href="..\dispmprt\ns-dispmprt-_dxgk_child_descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structures, each of which contains an identifier.

When you have finished using the target mode set object handle, you must release the handle by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpn_releasetargetmodeset.md">pfnReleaseTargetModeSet</a>. Target mode set objects are reference counted, so if you acquire a handle several times, you must release it that same number of times.

The lifetime of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_vidpntargetmodeset_interface.md">DXGK_VIDPNTARGETMODESET_INTERFACE</a> structure returned in <i>ppVidPnTargetModeSetInterface</i> is owned by the operating system. Using this ownership scheme, the operating system can switch to newer implementations at run time without breaking clients of the interface.

The D3DDDI_VIDEO_PRESENT_TARGET_ID data type is defined in <i>D3dukmdt.h</i>.

The D3DKMDT_HVIDPN and D3DKMDT_HVIDPNTARGETMODESET data types are defined in <i>D3dkmdt.h</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570559">VidPN Target Mode Set Interface</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpn_releasetargetmodeset.md">pfnReleaseTargetModeSet</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpn_createnewtargetmodeset.md">pfnCreateNewTargetModeSet</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpn_assigntargetmodeset.md">pfnAssignTargetModeSet</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPN_ACQUIRETARGETMODESET callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>