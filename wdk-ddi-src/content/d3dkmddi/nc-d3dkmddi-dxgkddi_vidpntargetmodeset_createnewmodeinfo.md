---
UID : NC:d3dkmddi.DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO
title : DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO
author : windows-driver-content
description : The pfnCreateNewModeInfo function returns a pointer to a D3DKMDT_VIDPN_TARGET_MODE structure that the display miniport driver populates before calling pfnAddMode.
old-location : display\dxgk_vidpntargetmodeset_interface_pfncreatenewmodeinfo.htm
old-project : display
ms.assetid : ebb37681-fa03-49f5-968b-87c9ff4ebae9
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
req.alt-api : pfnCreateNewModeInfo
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


# DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO callback function
The <b>pfnCreateNewModeInfo</b> function returns a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_target_mode.md">D3DKMDT_VIDPN_TARGET_MODE</a> structure that the display miniport driver populates before calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpntargetmodeset_addmode.md">pfnAddMode</a>.

## Syntax

```
DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO DxgkddiVidpntargetmodesetCreatenewmodeinfo;

NTSTATUS DxgkddiVidpntargetmodesetCreatenewmodeinfo(
  IN_CONST_D3DKMDT_HVIDPNTARGETMODESET hVidPnTargetModeSet,
  DEREF_OUT_PPD3DKMDT_VIDPN_TARGET_MODE ppNewVidPnTargetModeInfo
)
{...}
```

## Parameters

`hVidPnTargetModeSet`

[in] A handle to a VidPN target mode set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpn_acquiretargetmodeset.md">pfnAcquireTargetModeSet</a> function of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_vidpn_interface.md">DXGK_VIDPN_INTERFACE</a> interface.

`ppNewVidPnTargetModeInfo`

[out] A pointer to a variable that receives a pointer to a D3DKMDT_VIDPN_TARGET_MODE structure allocated by the VidPN manager.


## Return Value

The <b>pfnCreateNewModeInfo</b> function returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function succeeded. 
<dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TARGETMODESET</b></dt>
</dl>The handle supplied in <i>hVidPnTargetModeSet</i> was invalid.

## Remarks

The <b>pfnCreateNewModeInfo</b> function allocates a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_target_mode.md">D3DKMDT_VIDPN_TARGET_MODE</a> structure and sets its <b>Id</b> member to a newly generated identifier.

After you call <b>pfnCreateNewModeInfo</b> to obtain a D3DKMDT_VIDPN_TARGET_MODE structure, you must do one, but not both, of the following:

Populate the <b>Info</b> member of the structure and pass the structure to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpntargetmodeset_addmode.md">pfnAddMode</a>.

Release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpntargetmodeset_releasemodeinfo.md">pfnReleaseModeInfo</a>.

When you populate a D3DKMDT_VIDPN_TARGET_MODE structure, you have the option of overwriting the <b>Id</b> member that was generated and set by <b>pfnCreateNewModeInfo</b>. However, if you overwrite the <b>Id</b> member of any D3DKMDT_VIDPN_TARGET_MODE structure, you must overwrite the <b>Id</b> members of all the D3DKMDT_VIDPN_TARGET_MODE structures you obtain from <b>pfnCreateNewModeInfo</b>. Unless you have a specific reason for overwriting the <b>Id</b> members (for example, tracking target modes with your own numbering scheme), you should leave them as set by <b>pfnCreateNewModeInfo</b>.

The D3DKMDT_HVIDPNTARGETMODESET data type is defined in <i>D3dkmdt.h</i>.

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpntargetmodeset_addmode.md">pfnAddMode</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_vidpntargetmodeset_releasemodeinfo.md">pfnReleaseModeInfo</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_target_mode.md">D3DKMDT_VIDPN_TARGET_MODE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>