---
UID: NS:d3dkmddi._DXGK_SET_TIMING_PATH_INFO
title: "_DXGK_SET_TIMING_PATH_INFO"
author: windows-driver-content
description: Structure to hold information to modify SetTiming path.
old-location: display\dxgk_set_timing_path_info.htm
old-project: display
ms.assetid: 23B42F75-6313-430F-8CD3-EBAAE87C7815
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_SET_TIMING_PATH_INFO, DXGK_SET_TIMING_PATH_INFO structure [Display Devices], PDXGK_SET_TIMING_PATH_INFO, PDXGK_SET_TIMING_PATH_INFO structure pointer [Display Devices], _DXGK_SET_TIMING_PATH_INFO, d3dkmddi/DXGK_SET_TIMING_PATH_INFO, d3dkmddi/PDXGK_SET_TIMING_PATH_INFO, display.dxgk_set_timing_path_info
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
-	DXGK_SET_TIMING_PATH_INFO
product: Windows
targetos: Windows
req.typenames: DXGK_SET_TIMING_PATH_INFO
---

# _DXGK_SET_TIMING_PATH_INFO structure
Structure to hold information to modify SetTiming path.

## Syntax
```
typedef struct _DXGK_SET_TIMING_PATH_INFO {
  D3DDDI_VIDEO_PRESENT_TARGET_ID     VidPnTargetId;
  union {
    D3DDDI_COLOR_SPACE_TYPE             OutputColorSpace;
    D3DDDI_OUTPUT_WIRE_COLOR_SPACE_TYPE OutputWireColorSpace;
  };
  D3DKMDT_WIRE_FORMAT_AND_PREFERENCE SelectedWireFormat;
  union {
    struct {
      DXGK_PATH_UPDATE  : 2 VidPnPathUpdates;
      UINT  : 1             Active;
      UINT  : 1             IgnoreConnectivity;
      UINT  : 1             PreserveInherited;
      UINT  : 27            Reserved;
    } Input;
    UINT InputFlags;
  };
  union {
    struct {
      UINT  : 1  RecheckMPO;
      UINT  : 31 Reserved;
    } Output;
    UINT OutputFlags;
  };
  DXGK_CONNECTION_CHANGE             TargetState;
  union {
    struct {
      DXGK_GLITCH_CAUSE    GlitchCause;
      DXGK_GLITCH_EFFECT   GlitchEffect;
      DXGK_GLITCH_DURATION GlitchDuration;
      UINT8                Reserved;
    };
    UINT DiagnosticInfo;
  };
} DXGK_SET_TIMING_PATH_INFO;
```

## Members


`VidPnTargetId`

The identifier of a display adapter's video present target.

`SelectedWireFormat`

A <a href="https://msdn.microsoft.com/24CC6A10-6462-4681-B340-E887B679F456">D3DKMDT_WIRE_FORMAT_AND_PREFERENCE</a> value which indicates the wire format to be set for the path. The Preference field is reserved in this context so should be ignored by the driver.  In the remaining five bit-fields, the OS will set one of the thirty bits to indicate which color encoding and at which bit depth the link should be driven.

`TargetState`

Indicates the target state as a result of this call. Since changing timings may cause the connection state of both modified targets and targets which the OS did not intended to change, this field communicates the state for each path.  

If the target state is unchanged, this field should contain a copy of the last state reported on the target, including the same ConnectionChangeId which was previously reported.

If the target state is changed, this field should contain a copy of the queued, connection change which reflects the state resulting from the SetTiming call.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |