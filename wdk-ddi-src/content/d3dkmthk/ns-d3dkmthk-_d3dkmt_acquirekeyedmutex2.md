---
UID: NS:d3dkmthk._D3DKMT_ACQUIREKEYEDMUTEX2
title: "_D3DKMT_ACQUIREKEYEDMUTEX2"
author: windows-driver-content
description: Describes a keyed mutex object that the D3DKMTAcquireKeyedMutex2 function acquires that includes private data.
old-location: display\d3dkmt_acquirekeyedmutex2.htm
old-project: display
ms.assetid: 6e7ccf24-6403-44bf-9369-d2825646e950
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DKMT_ACQUIREKEYEDMUTEX2, D3DKMT_ACQUIREKEYEDMUTEX2 structure [Display Devices], _D3DKMT_ACQUIREKEYEDMUTEX2, d3dkmthk/D3DKMT_ACQUIREKEYEDMUTEX2, display.d3dkmt_acquirekeyedmutex2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3DKMT_ACQUIREKEYEDMUTEX2
product: Windows
targetos: Windows
req.typenames: D3DKMT_ACQUIREKEYEDMUTEX2
---

# _D3DKMT_ACQUIREKEYEDMUTEX2 structure
Describes a keyed mutex object that the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtacquirekeyedmutex2.md">D3DKMTAcquireKeyedMutex2</a> function acquires that includes private data.

## Syntax
````
typedef struct _D3DKMT_ACQUIREKEYEDMUTEX2 {
  D3DKMT_HANDLE  hKeyedMutex;
  UINT64         Key;
  PLARGE_INTEGER pTimeout;
  UINT64         FenceValue;
  VOID           *pPrivateRuntimeData;
  UINT           PrivateRuntimeDataSize;
} D3DKMT_ACQUIREKEYEDMUTEX2;
````

## Members


`hKeyedMutex`

[in] A D3DKMT_HANDLE data type that represents a handle to the keyed mutex.

`Key`

[in] The key value to acquire.

`pTimeout`

[in] An NT-style timeout value.

`FenceValue`

[out] The current fence value of the GPU sync object.

`pPrivateRuntimeData`

[out] A pointer to a buffer to copy private data to.

`PrivateRuntimeDataSize`

[in] The size, in bytes, of the <b>pPrivateRuntimeData</b> member.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtacquirekeyedmutex2.md">D3DKMTAcquireKeyedMutex2</a>