---
UID: NS:d3dkmthk._D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
title: "_D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2"
author: windows-driver-content
description: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 is used with D3DKMTOpenSyncObjectFromNtHandle2 to open a monitored fence object.
old-location: display\d3dkmt_opensyncobjectfromnthandle2.htm
old-project: display
ms.assetid: 7C5F9ACF-AA21-4A2B-B943-3B1D940284E1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2, D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure [Display Devices], _D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2, d3dkmthk/D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2, display.d3dkmt_opensyncobjectfromnthandle2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	D3dkmthk.h
api_name:
-	D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
product: Windows
targetos: Windows
req.typenames: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
---

# _D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure
<b>D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2</b> is used with <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle2.md">D3DKMTOpenSyncObjectFromNtHandle2</a> to open a monitored fence object.

## Syntax
````
typedef struct _D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 {
  HANDLE                             hNtHandle;
  D3DKMT_HANDLE                      hDevice;
  D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS Flags;
  D3DKMT_HANDLE                      hSyncObject;
  union {
    struct {
      VOID                   *FenceValueCPUVirtualAddress;
      D3DGPU_VIRTUAL_ADDRESS FenceValueGPUVirtualAddress;
      UINT                   EngineAffinity;
    } MonitoredFence;
    UINT64 Reserved[8];
  };
} D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2;
````

## Members


`hNtHandle`

[in] NT handle for the sync object to be opened.

`hDevice`

[in] Device handle to use this sync object on.

`Flags`

[in] Specifies the desired sync object behavior for this device, such as wait and signal semantics and TDR handling.

`hSyncObject`

[out] Handle to the sync object that can be used in this process.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle2.md">D3DKMTOpenSyncObjectFromNtHandle2</a>