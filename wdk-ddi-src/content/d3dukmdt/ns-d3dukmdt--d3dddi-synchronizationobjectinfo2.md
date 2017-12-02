---
UID: NS.d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECTINFO2
title: D3DDDI_SYNCHRONIZATIONOBJECTINFO2
author: windows-driver-content
description: The D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure contains information about a second-generation synchronization object.
old-location: display\d3dddi_synchronizationobjectinfo2.htm
old-project: display
ms.assetid: dc1c6a67-320c-41f8-91ad-cdbcde191a81
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_SYNCHRONIZATIONOBJECTINFO2, D3DDDI_SYNCHRONIZATIONOBJECTINFO2
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
req.alt-api: D3DDDI_SYNCHRONIZATIONOBJECTINFO2
req.alt-loc: d3dukmdt.h
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
req.iface: 
---

# D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure



## -description
<p>The <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> structure contains information about a second-generation synchronization object.</p>


## -syntax

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


## -struct-fields
<dl>

### -field Type

<dd>
<p>[in] A value of type <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-synchronizationobject-type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a> that indicates the type of synchronization object.</p>
</dd>

### -field Flags

<dd>
<p>[in] A <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-synchronizationobject-flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a> structure that specifies, in bit-field flags, attributes of the synchronization object. </p>
</dd>

### -field SynchronizationMutex

<dd>
<p>A structure that contains information about a synchronization mutex. If the <b>Type</b> member is equal to <b>D3DDDI_SYNCHRONIZATION_MUTEX</b>, the union in <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> holds a <b>SynchronizationMutex</b> structure, which contains the following member:</p>
<dl>

### -field InitialState

<dd>
<p>A Boolean value that indicates whether the synchronization mutex is initially owned by an object. A value of <b>TRUE</b> indicates that the mutex is owned; <b>FALSE</b> indicates that the mutex is not owned. </p>
</dd>
</dl>
</dd>

### -field Semaphore

<dd>
<p>A structure that contains information about a semaphore. If the <b>Type</b> member is equal to <b>D3DDDI_SEMAPHORE</b>, the union in <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> holds a <b>Semaphore</b> structure, which contains the following members:</p>
<dl>

### -field MaxCount

<dd>
<p>The maximum number of events that an object can be waiting for. </p>
</dd>

### -field InitialCount

<dd>
<p>The initial number of events that an object is waiting for. </p>
</dd>
</dl>
</dd>

### -field Fence

<dd>
<p>A structure that contains information about a fence. If the <b>Type</b> member is equal to <b>D3DDDI_FENCE</b>, the union in <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> holds a <b>Fence</b> structure, which contains the following member:</p>
<dl>

### -field FenceValue

<dd>
<p>A 64-bit value that specifies the initial fence value. </p>
</dd>
</dl>
</dd>

### -field CPUNotification

<dd>
<p>A structure that contains information about a CPU notification. If the <b>Type</b> member is equal to <b>D3DDDI_CPU_NOTIFICATION</b>, the union in <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> holds a <b>CPUNotification</b> structure, which contains the following member:</p>
<dl>

### -field Event

<dd>
<p>The handle to the CPU notification event. </p>
</dd>
</dl>
</dd>

### -field MonitoredFence

<dd>
<p>A structure that contains information about a monitored fence. If the <b>Type</b> member is equal to <b>D3DDDI_MONITORED_FENCE</b>, the union in <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> holds a <b>MonitoredFence</b> structure.</p>
<p>Supported starting with Windows 10.</p>
<dl>

### -field InitialFenceValue

<dd>
<p>[in] A 64-bit value that specifies the initial fence value. </p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field FenceValueCPUVirtualAddress

<dd>
<p>[out] A read-only mapping of the fence value for the CPU. This is a user mode address readable from the process that created the monitored fence object. For 32 bit platforms that support 64 bit atomic reads via methods such as <code>InterlockedCompareExchange64(pointer,0,0)</code>, the mapping will be made read-write instead of read-only to avoid an access violation during the interlocked operation. Depending on the value of <b>No64BitAtomics</b> cap, this address points to either a 32 bit or a 64 bit underlying value.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field FenceValueGPUVirtualAddress

<dd>
<p>[out] A read-write mapping of the fence value for the GPU. A driver can signal a new fence value by inserting a GPU write command for this address into a command buffer, and the DirectX graphics kernel will unblock waiters for this fence object value. Depending on the value of <b>No64BitAtomics</b> cap, this address points to either a 32 bit or a 64 bit underlying value.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field EngineAffinity

<dd>
<p>[in] A bit field, where each bit position (starting from zero) defines a physical adapter index in an link display adapter (LDA) link where the GPU virtual address will be committed. Zero means that the GPU virtual address will be committed to all physical adapters.</p>
<p>Supported starting with Windows 10.</p>
</dd>
</dl>
</dd>

### -field PeriodicMonitoredFence

<dd>
<p>A structure that contains information about a periodic monitored fence. If the <b>Type</b> member is equal to <b>D3DDDI_PERIODIC_MONITORED_FENCE</b>, the union in <b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> holds a <b>MonitoredFence</b> structure.</p>
<p>Supported starting with Windows 10.</p>
<dl>

### -field hAdapter

<dd>
<p>[in] A handle to the adapter associated with VidPnSourceID</p>
</dd>

### -field 	VidPnTargetID

<dd>
<p>[out] The output ID that the compositor wishes to receive notifications for.</p>
</dd>

### -field Time

<dd>
<p>[out] Represents an offset before the VSync (time of VSync – Time parameter). The Time value may not be longer than a VSync interval (1 / DisplayModeRefresh). Time is specified in units of 100ns.</p>
</dd>

### -field FenceValueCPUVirtualAddress

<dd>
<p>[in] Read-only mapping of the fence value for the CPU</p>
</dd>

### -field FenceValueGPUVirtualAddress

<dd>
<p>[in] Read-only mapping of the fence value for the GPU</p>
</dd>

### -field EngineAffinity

<dd>
<p>[in] Defines physical adapters where the GPU VA will be mapped</p>
</dd>
</dl>
</dd>

### -field Reserved

<dd>
<p>A structure that is reserved for future use. This structure contains the following member:</p>
<dl>

### -field Reserved

<dd>
<p>An array of 64-bit values that are reserved for future use.</p>
</dd>
</dl>
</dd>

### -field SharedHandle

<dd>
<p>[out] A handle to the shared synchronization object if a shared handle currently exists. The shared handle is returned from the call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md">D3DKMTCreateSynchronizationObject2</a> function. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p><b>D3DDDI_SYNCHRONIZATIONOBJECTINFO2</b> is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-synchronizationobject-flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-synchronizationobject-type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-createsynchronizationobject2.md">D3DKMT_CREATESYNCHRONIZATIONOBJECT2</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatesynchronizationobject2.md">D3DKMTCreateSynchronizationObject2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
