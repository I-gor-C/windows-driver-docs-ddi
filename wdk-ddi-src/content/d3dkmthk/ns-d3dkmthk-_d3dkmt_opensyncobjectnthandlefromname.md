---
UID: NS:d3dkmthk._D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
title: "_D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME"
author: windows-driver-content
description: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME is used with D3DKMTOpenSyncObjectNtHandleFromName to open an NT handle for a named shared monitored fence object.
old-location: display\d3dkmt_opensyncobjectnthandlefromname.htm
old-project: display
ms.assetid: 6435D3B7-A1B7-4417-8272-C505A5FA500E
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME, D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME structure [Display Devices], _D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME, d3dkmthk/D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME, display.d3dkmt_opensyncobjectnthandlefromname
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
-	D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
product: Windows
targetos: Windows
req.typenames: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
---

# _D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME structure
<b>D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906779">D3DKMTOpenSyncObjectNtHandleFromName</a> to open an NT handle for a named shared monitored fence object.

## Syntax
```
typedef struct _D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME {
  DWORD             dwDesiredAccess;
  OBJECT_ATTRIBUTES *pObjAttrib;
  HANDLE            hNtHandle;
} D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME;
```

## Members


`dwDesiredAccess`

[in] Access attributes for opening a shared monitored fence sync object, such as <b>D3DDDI_SYNC_OBJECT_WAIT</b>, <b>D3DDDI_SYNC_OBJECT_SIGNAL</b>, or <b>D3DDDI_SYNC_OBJECT_ALL_ACCESS</b>.

`pObjAttrib`

[in] Object attributes for opening the object handle, including the shared object name information.

`hNtHandle`

[out] NT handle to the sync object that can be used to open it via <a href="https://msdn.microsoft.com/library/windows/hardware/dn906778">D3DKMTOpenSyncObjectFromNtHandle2</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906778">D3DKMTOpenSyncObjectFromNtHandle2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn906779">D3DKMTOpenSyncObjectNtHandleFromName</a>