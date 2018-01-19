---
UID : NS:d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECTINFO2
title : _D3DDDI_SYNCHRONIZATIONOBJECTINFO2
author : windows-driver-content
description : The D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure contains information about a second-generation synchronization object.
old-location : display\d3dddi_synchronizationobjectinfo2.htm
old-project : display
ms.assetid : dc1c6a67-320c-41f8-91ad-cdbcde191a81
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DDDI_SYNCHRONIZATIONOBJECTINFO2, D3DDDI_SYNCHRONIZATIONOBJECTINFO2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dukmdt.h
req.include-header : D3dumddi.h, D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : D3DDDI_SYNCHRONIZATIONOBJECTINFO2 is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DDDI_SYNCHRONIZATIONOBJECTINFO2
req.alt-loc : d3dukmdt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3DDDI_SYNCHRONIZATIONOBJECTINFO2
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

        
            `Flags`

            [in] A <a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_synchronizationobject_flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a> structure that specifies, in bit-field flags, attributes of the synchronization object.
        
            `SharedHandle`

            [out] A handle to the shared synchronization object if a shared handle currently exists. The shared handle is returned from the call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md">D3DKMTCreateSynchronizationObject2</a> function.
        
            `Type`

            [in] A value of type <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddi_synchronizationobject_type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a> that indicates the type of synchronization object.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_synchronizationobject_flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt-_d3dddi_synchronizationobject_type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createsynchronizationobject2.md">D3DKMT_CREATESYNCHRONIZATIONOBJECT2</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md">D3DKMTCreateSynchronizationObject2</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>