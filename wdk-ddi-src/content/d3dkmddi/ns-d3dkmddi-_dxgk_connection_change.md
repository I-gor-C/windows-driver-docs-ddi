---
UID: NS:d3dkmddi._DXGK_CONNECTION_CHANGE
title: "_DXGK_CONNECTION_CHANGE"
author: windows-driver-content
description: Structure to describe the most recently updated status of the link for a target.
old-location: display\dxgk_connection_change.htm
old-project: display
ms.assetid: 0B0D640C-3E4B-4DE0-AA11-C751F210C77A
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PDXGK_CONNECTION_CHANGE, DXGK_CONNECTION_CHANGE, DXGK_CONNECTION_CHANGE structure [Display Devices], PDXGK_CONNECTION_CHANGE, PDXGK_CONNECTION_CHANGE structure pointer [Display Devices], _DXGK_CONNECTION_CHANGE, d3dkmddi/DXGK_CONNECTION_CHANGE, d3dkmddi/PDXGK_CONNECTION_CHANGE, display.dxgk_connection_change"
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
-	DXGK_CONNECTION_CHANGE
product: Windows
targetos: Windows
req.typenames: DXGK_CONNECTION_CHANGE, *PDXGK_CONNECTION_CHANGE
---

# _DXGK_CONNECTION_CHANGE structure
Structure to describe the most recently updated status of the link for a target.

## Syntax
````
typedef struct _DXGK_CONNECTION_CHANGE {
  ULONGLONG                      ConnectionChangeId  :24;
  D3DDDI_VIDEO_PRESENT_TARGET_ID TargetId  :4;
  DXGK_CONNECTION_STATUS         ConnectionStatus  :4;
  ULONG                          Reserved;
  union {
    struct {
      D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY MonitorConnect.LinkTargetType;
    } MonitorConnect;
    struct {
      D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY TargetConnect.BaseTargetType;
      D3DDDI_VIDEO_PRESENT_TARGET_ID  TargetConnect.NewTargetId;
    } TargetConnect;
    struct {
      D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY TargetJoin.BaseTargetType;
      D3DDDI_VIDEO_PRESENT_TARGET_ID  TargetJoin.NewTargetId;
    } TargetJoin;
  };
} DXGK_CONNECTION_CHANGE, *PDXGK_CONNECTION_CHANGE;
````

## Members


`ConnectionChangeId`

The per target unique id for the transition being reported.  This value must be unique across all targets on the adapter and must be monotonically increasing for each change reported.

`ConnectionStatus`

The status of the connection.

`Reserved`

This value is reserved for system use.

`TargetId`

The target id for which the change is being reported.  This target id must have been reported to the OS before and must be in a state which supports the given change.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |