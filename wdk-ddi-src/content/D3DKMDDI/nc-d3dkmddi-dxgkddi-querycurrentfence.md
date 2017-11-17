---
UID: NC.d3dkmddi.DXGKDDI_QUERYCURRENTFENCE
title: DXGKDDI_QUERYCURRENTFENCE
author: windows-driver-content
description: The DxgkDdiQueryCurrentFence function queries about the latest completed submission fence identifier in the hardware command execution unit.
old-location: display\dxgkddiquerycurrentfence.htm
ms.assetid: 0ca4d42f-3036-4b81-91a4-fbce7ac891fe
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiQueryCurrentFence
req.alt-loc: D3dkmddi.h
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGKDDI_QUERYCURRENTFENCE callback



## -description
<p>The <i>DxgkDdiQueryCurrentFence</i> function queries about the latest completed submission fence identifier in the hardware command execution unit.</p>


## -prototype

````
DXGKDDI_QUERYCURRENTFENCE DxgkDdiQueryCurrentFence;

NTSTATUS  APIENTRY DxgkDdiQueryCurrentFence(
   const HANDLE                    hAdapter,
         DXGKARG_QUERYCURRENTFENCE *pCurrentFence
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> 

<dd>
<p>[in] A handle to a context block that is associated with a display adapter. The display miniport driver previously provided this handle to the Microsoft DirectX graphics kernel subsystem in the <i>MiniportDeviceContext</i> output parameter of the <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function.</p>
</dd>

### -param <i>pCurrentFence</i> 

<dd>
<p>[in/out] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff557624">DXGKARG_QUERYCURRENTFENCE</a> structure that contains information about the current fence data. </p>
</dd>
</dl>

## -returns
<p><i>DxgkDdiQueryCurrentFence</i> returns STATUS_SUCCESS, or an appropriate error result if the fence data is not successfully retrieved.</p>

## -remarks
<p>A <i>fence</i> is an instruction that contains 64 bits of data and an address. The display miniport driver can insert a fence in the direct memory access (DMA) stream that is sent to the graphics processing unit (GPU). When the GPU reads the fence, the GPU writes the fence data at the specified fence address. However, before the GPU can write the fence data to memory, it must ensure that all of the pixels from the primitives that precede the fence instruction are retired and properly written to memory. </p>

<p>Hardware that supports per-GPU-context virtual address space must support the following types of fences:</p>

<p><i>Regular fences </i>are fences that can be inserted in a DMA buffer that is created in user mode. Because the content of a DMA buffer from user mode is not trusted, fences within such a DMA buffer must refer to a virtual address in the GPU context address space and not to a physical address. Access to such a virtual address is bound by the same memory validation mechanism as any other virtual address that the GPU accesses.</p>

<p><i>Privileged fences</i> are fences that can be inserted only in a DMA buffer that is created (and only accessible) in kernel mode. Fences within such a DMA buffer refer to a physical address in memory. </p>

<p>Note that if the fence target address was accessible in user mode, malicious software could perform a graphics operation over the memory location for the fence and therefore override the content of what the kernel expected to receive.</p>

<p>Note that a privileged DMA buffer can contain both regular and privileged fences. However, if a privileged DMA buffer contains a regular fence, the kernel component that generated such a DMA buffer is aware that the regular fence inside might never be accessible.</p>

<p>If the display miniport driver missed the last fence of a DMA buffer, the driver's <i>DxgkDdiQueryCurrentFence</i> function might be called to report the missed fence. For example, if the hardware generates a fence to memory, the driver's <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a> function is triggered to read the memory. However, if the fence's data is not available when the driver attempts to read the data (for example, if there is a defective chipset), the fence is typically reported at the next interrupt, unless interrupts were stopped. If interrupts were stopped and the DirectX graphics kernel subsystem waits too long for a fence, the subsystem calls the driver's <i>DxgkDdiQueryCurrentFence</i> function to verify the current fence and determine any pending fence that it might have missed.</p>

<p>Before the display miniport driver returns from a call to <i>DxgkDdiQueryCurrentFence</i>, if the latest hardware-completed submission fence identifier has not yet been reported, the driver must call the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function to report the fence. To implement this functionality, the driver:</p>

<p>Tracks which fence was last reported to the operating system.</p>

<p>Raises IRQL to device interrupt. To raise IRQL to interrupt level, the driver can call the <a href="https://msdn.microsoft.com/9c659319-d0a5-43a7-b9a9-9fad18397a09">DxgkCbSynchronizeExecution</a> function to synchronize with its <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a> function.</p>

<p>At device interrupt IRQL, compares the last reported fence with the latest hardware-completed fence.</p>

<p>At device interrupt IRQL, calls <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> only when the latest hardware completed fence is newer than the last reported fence.</p>

<p><i>DxgkDdiQueryCurrentFence</i> should be made pageable.</p>

<p>A <i>fence</i> is an instruction that contains 64 bits of data and an address. The display miniport driver can insert a fence in the direct memory access (DMA) stream that is sent to the graphics processing unit (GPU). When the GPU reads the fence, the GPU writes the fence data at the specified fence address. However, before the GPU can write the fence data to memory, it must ensure that all of the pixels from the primitives that precede the fence instruction are retired and properly written to memory. </p>

<p>Hardware that supports per-GPU-context virtual address space must support the following types of fences:</p>

<p><i>Regular fences </i>are fences that can be inserted in a DMA buffer that is created in user mode. Because the content of a DMA buffer from user mode is not trusted, fences within such a DMA buffer must refer to a virtual address in the GPU context address space and not to a physical address. Access to such a virtual address is bound by the same memory validation mechanism as any other virtual address that the GPU accesses.</p>

<p><i>Privileged fences</i> are fences that can be inserted only in a DMA buffer that is created (and only accessible) in kernel mode. Fences within such a DMA buffer refer to a physical address in memory. </p>

<p>Note that if the fence target address was accessible in user mode, malicious software could perform a graphics operation over the memory location for the fence and therefore override the content of what the kernel expected to receive.</p>

<p>Note that a privileged DMA buffer can contain both regular and privileged fences. However, if a privileged DMA buffer contains a regular fence, the kernel component that generated such a DMA buffer is aware that the regular fence inside might never be accessible.</p>

<p>If the display miniport driver missed the last fence of a DMA buffer, the driver's <i>DxgkDdiQueryCurrentFence</i> function might be called to report the missed fence. For example, if the hardware generates a fence to memory, the driver's <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a> function is triggered to read the memory. However, if the fence's data is not available when the driver attempts to read the data (for example, if there is a defective chipset), the fence is typically reported at the next interrupt, unless interrupts were stopped. If interrupts were stopped and the DirectX graphics kernel subsystem waits too long for a fence, the subsystem calls the driver's <i>DxgkDdiQueryCurrentFence</i> function to verify the current fence and determine any pending fence that it might have missed.</p>

<p>Before the display miniport driver returns from a call to <i>DxgkDdiQueryCurrentFence</i>, if the latest hardware-completed submission fence identifier has not yet been reported, the driver must call the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function to report the fence. To implement this functionality, the driver:</p>

<p>Tracks which fence was last reported to the operating system.</p>

<p>Raises IRQL to device interrupt. To raise IRQL to interrupt level, the driver can call the <a href="https://msdn.microsoft.com/9c659319-d0a5-43a7-b9a9-9fad18397a09">DxgkCbSynchronizeExecution</a> function to synchronize with its <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a> function.</p>

<p>At device interrupt IRQL, compares the last reported fence with the latest hardware-completed fence.</p>

<p>At device interrupt IRQL, calls <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> only when the latest hardware completed fence is newer than the last reported fence.</p>

<p><i>DxgkDdiQueryCurrentFence</i> should be made pageable.</p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557624">DXGKARG_QUERYCURRENTFENCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9c659319-d0a5-43a7-b9a9-9fad18397a09">DxgkCbSynchronizeExecution</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_QUERYCURRENTFENCE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
