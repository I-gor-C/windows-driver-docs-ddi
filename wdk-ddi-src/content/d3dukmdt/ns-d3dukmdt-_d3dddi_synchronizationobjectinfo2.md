---
UID: NS:d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECTINFO2
title: "_D3DDDI_SYNCHRONIZATIONOBJECTINFO2"
author: windows-driver-content
description: The D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure contains information about a second-generation synchronization object.
old-location: display\d3dddi_synchronizationobjectinfo2.htm
old-project: display
ms.assetid: dc1c6a67-320c-41f8-91ad-cdbcde191a81
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDI_SYNCHRONIZATIONOBJECTINFO2, D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure [Display Devices], D3D_other_Structs_0efa3a96-3e04-4232-bf7a-53c3f038d6ec.xml, _D3DDDI_SYNCHRONIZATIONOBJECTINFO2, d3dukmdt/D3DDDI_SYNCHRONIZATIONOBJECTINFO2, display.d3dddi_synchronizationobjectinfo2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDI_SYNCHRONIZATIONOBJECTINFO2 is supported beginning with the Windows 7 operating system.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dukmdt.h
api_name:
-	D3DDDI_SYNCHRONIZATIONOBJECTINFO2
product: Windows
targetos: Windows
req.typenames: D3DDDI_SYNCHRONIZATIONOBJECTINFO2
---

# _D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure
The <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> structure contains information about a second-generation synchronization object.

## Syntax
````
typedef struct _D3DDDI_SYNCHRONIZATIONOBJECTINFO2 {
  D3DDDI_SYNCHRONIZATIONOBJECT_TYPE  Type;
  D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS Flags;
  union {
    struct {
      BOOL InitialState;
    } SynchronizationMutex;
    struct {
      UINT MaxCount;
      UINT InitialCount;
    } Semaphore;
    struct {
      UINT64 FenceValue;
    } Fence;
    struct {
      HANDLE Event;
    } CPUNotification;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0))
    struct {
      UINT64                 InitialFenceValue;
      VOID                   *FenceValueCPUVirtualAddress;
      D3DGPU_VIRTUAL_ADDRESS FenceValueGPUVirtualAddress;
      UINT                   EngineAffinity;
    } MonitoredFence;
#endif 
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_2))
    struct {
      D3DKMT_HANDLE                  hAdapter;
      D3DDDI_VIDEO_PRESENT_TARGET_ID 	VidPnTargetID;
      UINT64                         Time;
      VOID                           *FenceValueCPUVirtualAddress;
      D3DGPU_VIRTUAL_ADDRESS         FenceValueGPUVirtualAddress;
      UINT                           EngineAffinity;
    } PeriodicMonitoredFence;
    struct {
      UINT64 Reserved[8];
    } Reserved;
  };
  D3DKMT_HANDLE                      SharedHandle;
} D3DDDI_SYNCHRONIZATIONOBJECTINFO2;
````

## Members


`Type`

[in] A value of type <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddi_synchronizationobject_type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a> that indicates the type of synchronization object.

`Flags`

[in] A <a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_synchronizationobject_flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a> structure that specifies, in bit-field flags, attributes of the synchronization object.

`SharedHandle`

[out] A handle to the shared synchronization object if a shared handle currently exists. The shared handle is returned from the call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md">D3DKMTCreateSynchronizationObject2</a> function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DDDI_SYNCHRONIZATIONOBJECTINFO2 is supported beginning with the Windows 7 operating system. D3DDDI_SYNCHRONIZATIONOBJECTINFO2 is supported beginning with the Windows 7 operating system. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_synchronizationobject_flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a>



<a href="..\d3dukmdt\ne-d3dukmdt-_d3dddi_synchronizationobject_type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a>



<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createsynchronizationobject2.md">D3DKMT_CREATESYNCHRONIZATIONOBJECT2</a>



<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md">D3DKMTCreateSynchronizationObject2</a>