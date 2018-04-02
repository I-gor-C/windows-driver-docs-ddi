---
UID: NS:d3dkmthk._D3DKMT_OPENRESOURCEFROMNTHANDLE
title: "_D3DKMT_OPENRESOURCEFROMNTHANDLE"
author: windows-driver-content
description: Describes information that is required to open a shared resource from an NT handle to the process. The shared resource can be a set of allocations, a keyed mutex, or a synchronization object.
old-location: display\d3dkmt_openresourcefromnthandle.htm
old-project: display
ms.assetid: 3f595816-29b5-4efc-a00c-77597dd9fa48
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_OPENRESOURCEFROMNTHANDLE, D3DKMT_OPENRESOURCEFROMNTHANDLE structure [Display Devices], _D3DKMT_OPENRESOURCEFROMNTHANDLE, d3dkmthk/D3DKMT_OPENRESOURCEFROMNTHANDLE, display.d3dkmt_openresourcefromnthandle
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
-	D3DKMT_OPENRESOURCEFROMNTHANDLE
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_OPENRESOURCEFROMNTHANDLE
---

# _D3DKMT_OPENRESOURCEFROMNTHANDLE structure
Describes information that is required to open a shared resource from an NT handle to the process. The shared resource can be a set of allocations, a keyed mutex, or a synchronization object.

## Syntax
```
typedef struct _D3DKMT_OPENRESOURCEFROMNTHANDLE {
  D3DKMT_HANDLE              hDevice;
  HANDLE                     hNtHandle;
  UINT                       NumAllocations;
  D3DDDI_OPENALLOCATIONINFO2 *pOpenAllocationInfo2;
  UINT                       PrivateRuntimeDataSize;
  VOID                       *pPrivateRuntimeData;
  UINT                       ResourcePrivateDriverDataSize;
  VOID                       *pResourcePrivateDriverData;
  UINT                       TotalPrivateDriverDataBufferSize;
  VOID                       *pTotalPrivateDriverDataBuffer;
  D3DKMT_HANDLE              hResource;
  D3DKMT_HANDLE              hKeyedMutex;
  VOID                       *pKeyedMutexPrivateRuntimeData;
  UINT                       KeyedMutexPrivateRuntimeDataSize;
  D3DKMT_HANDLE              hSyncObject;
} D3DKMT_OPENRESOURCEFROMNTHANDLE;
```

## Members


`hDevice`

[in] A D3DKMT_HANDLE data type that represents the device.

`hNtHandle`

[in] An NT handle to the process.

`NumAllocations`

[in] The number of allocations associated with the resource.

`pOpenAllocationInfo2`

[in] This member is reserved and should be set to zero.

`PrivateRuntimeDataSize`

[in] The size, in bytes, of the buffer pointed to by the <b>pPrivateRuntimeData</b> member.

`pPrivateRuntimeData`

[in] A caller-supplied buffer where the runtime private data associated with this resource will be copied to.

`ResourcePrivateDriverDataSize`

[in] The size, in bytes, of the  buffer pointed to by the <b>pResourcePrivateDriverData</b> member.

`pResourcePrivateDriverData`

[in] A caller-supplied buffer where the driver private data associated with the resource will be copied to.

`TotalPrivateDriverDataBufferSize`

[in] The size, in bytes, of the buffer pointed to by the <b>pTotalPrivateDriverDataBuffer</b> member.

[out] The size, in bytes, of  the data written to <b>pTotalPrivateDriverDataBuffer</b>.

`pTotalPrivateDriverDataBuffer`

[in] A pointer to a caller-supplied buffer where the driver private data will be stored.

`hResource`

[out] A handle to the resource in this process.

`hKeyedMutex`

[out] A handle to the keyed mutex in this process.

`pKeyedMutexPrivateRuntimeData`

[in] A buffer that contains initial private data.

The data in this buffer will be copied only if the keyed mutex does not already have private data.

If this member has a value of <b>NULL</b>, the value of the <b>KeyedMutexPrivateRuntimeDataSize</b> member must be zero.

`KeyedMutexPrivateRuntimeDataSize`

[in] The size, in bytes, of the buffer pointed to by the <b>pKeyedMutexPrivateRuntimeData</b> member.

`hSyncObject`

[out] A handle to the synchronization object in this process.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439280">D3DDDI_OPENALLOCATIONINFO2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439409">D3DKMTOpenNtHandleFromName</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh780251">D3DKMTShareObjects</a>