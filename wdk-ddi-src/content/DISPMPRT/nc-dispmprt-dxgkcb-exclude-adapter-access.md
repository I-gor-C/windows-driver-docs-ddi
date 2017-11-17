---
UID: NC.dispmprt.DXGKCB_EXCLUDE_ADAPTER_ACCESS
title: DXGKCB_EXCLUDE_ADAPTER_ACCESS
author: windows-driver-content
description: The DxgkCbExcludeAdapterAccess function prevents all access to the display adapter and calls a provided DxgkProtectedCallback callback routine while in this protected state.
old-location: display\dxgkcbexcludeadapteraccess.htm
ms.assetid: e74e79fe-3b36-427e-ae0b-4072a0438c4e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbExcludeAdapterAccess
req.alt-loc: dispmprt.h
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
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKCB_EXCLUDE_ADAPTER_ACCESS callback



## -description
<p>The <b>DxgkCbExcludeAdapterAccess</b> function prevents all access to the display adapter and calls a provided <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> callback routine while in this protected state.</p>


## -prototype

````
DXGKCB_EXCLUDE_ADAPTER_ACCESS DxgkCbExcludeAdapterAccess;

NTSTATUS DxgkCbExcludeAdapterAccess(
  _In_ HANDLE                     DeviceHandle,
  _In_ ULONG                      Attributes,
  _In_ DXGKDDI_PROTECTED_CALLBACK DxgkProtectedCallback,
  _In_ PVOID                      ProtectedCallbackContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceHandle</i> [in]

<dd>
<p>A handle that represents a display adapter. The display miniport driver obtained this handle in the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure that was passed to <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a>.</p>
</dd>

### -param <i>Attributes</i> [in]

<dd>
<p>A value that specifies video memory operations. This parameter can be any combination of the following bit flag values, except that DXGK_EXCLUDE_EVICT_ALL and DXGK_EXCLUDE_CALL_SYNCHRONOUS are mutually exclusive. These values are defined in <i>Dispmprt.h</i>.</p>
<p></p>
<dl>

### -param <a id="DXGK_EXCLUDE_EVICT_ALL"></a><a id="dxgk_exclude_evict_all"></a>DXGK_EXCLUDE_EVICT_ALL

<dd>
<p>All video memory in the adapter is copied to system memory; this is an expensive operation. If the <i>Attributes</i> parameter is not set to this value, access to locked surfaces in system memory is suspended.</p>
</dd>

### -param <a id="DXGK_EXCLUDE_CALL_SYNCHRONOUS"></a><a id="dxgk_exclude_call_synchronous"></a>DXGK_EXCLUDE_CALL_SYNCHRONOUS

<dd>
<p>Executes the protected <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> driver callback routine in the same thread context as the caller. The caller must be calling from a <a href="https://msdn.microsoft.com/2b7c1eae-6527-469e-a2fa-74d2a1246bd3">second level</a> or <a href="https://msdn.microsoft.com/780d37d9-40c6-4737-9042-473810868227">third level</a> synchronized DDI call. Otherwise the <b>DxgkCbExcludeAdapterAccess</b> function will fail.</p>
</dd>

### -param <a id="DXGK_EXCLUDE_BRIDGE_ACCESS"></a><a id="dxgk_exclude_bridge_access"></a>DXGK_EXCLUDE_BRIDGE_ACCESS

<dd>
<p>Protects access to the PCI Express (PCIe) root port when the driver needs to access the root port configuration space. Set the <i>Attributes</i> parameter to this value before calling <a href="https://msdn.microsoft.com/118ea0b9-6463-4050-9f33-192a3d42fdce">DxgkCbReadDeviceSpace</a> or <a href="https://msdn.microsoft.com/797d6b0c-91a4-4923-ad40-937cfde50067">DxgkCbWriteDeviceSpace</a> functions with the <i>DataType</i> parameter set to DXGK_WHICHSPACE_BRIDGE.</p>
</dd>
</dl>
</dd>

### -param <i>DxgkProtectedCallback</i> [in]

<dd>
<p>The callback routine to be called back when all access to the adapter has been halted.</p>
</dd>

### -param <i>ProtectedCallbackContext</i> [in]

<dd>
<p>A pointer to the value to pass to the <i>ProtectedCallbackContext</i> parameter of the <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> callback routine.</p>
</dd>
</dl>

## -returns
<p><b>DxgkCbExcludeAdapterAccess</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in <i>Ntstatus.h</i>.</p>

## -remarks
<p>Application requests will be blocked until this function returns. While in this protective state, the provided <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> callback routine is called at IRQL = PASSIVE_LEVEL.</p>

<p><b>DxgkCbExcludeAdapterAccess</b> acquires exclusive adapter access in order to prevent graphics-related I/O operations to the display adapter and all links. This effectively idles the GPU for the entire duration of the call.</p>

<p>This function also prevents all PCI configuration space access to the PCI Express (PCIe) root port if DXGK_EXCLUDE_BRIDGE_ACCESS is specified in the <i>Attributes</i> parameter.</p>

<p>The driver should not block continued execution of the calling thread by waiting for the <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> callback routine to return. For example, the driver could schedule an asynchronous worker thread to handle the callback routine.</p>

<p>An exception to this blocking of application requests occurs when the user-mode display driver has set the <b>UseAlternateVA</b> bit-field flag in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544214">D3DDDICB_LOCKFLAGS</a> structure in a call to the <a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a> function. <b>DxgkCbExcludeAdapterAccess</b> does not block this type of allocation lock, and the CPU can access the display adapter while the protected callback routine is executing.</p>

<p>Application requests will be blocked until this function returns. While in this protective state, the provided <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> callback routine is called at IRQL = PASSIVE_LEVEL.</p>

<p><b>DxgkCbExcludeAdapterAccess</b> acquires exclusive adapter access in order to prevent graphics-related I/O operations to the display adapter and all links. This effectively idles the GPU for the entire duration of the call.</p>

<p>This function also prevents all PCI configuration space access to the PCI Express (PCIe) root port if DXGK_EXCLUDE_BRIDGE_ACCESS is specified in the <i>Attributes</i> parameter.</p>

<p>The driver should not block continued execution of the calling thread by waiting for the <a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a> callback routine to return. For example, the driver could schedule an asynchronous worker thread to handle the callback routine.</p>

<p>An exception to this blocking of application requests occurs when the user-mode display driver has set the <b>UseAlternateVA</b> bit-field flag in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544214">D3DDDICB_LOCKFLAGS</a> structure in a call to the <a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a> function. <b>DxgkCbExcludeAdapterAccess</b> does not block this type of allocation lock, and the CPU can access the display adapter while the protected callback routine is executing.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/7e282ec6-c159-47a4-af14-2b0cb8e34a8e">DxgkProtectedCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_EXCLUDE_ADAPTER_ACCESS callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
