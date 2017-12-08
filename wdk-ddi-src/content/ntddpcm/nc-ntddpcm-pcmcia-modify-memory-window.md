---
UID: NC.ntddpcm.PCMCIA_MODIFY_MEMORY_WINDOW
title: PCMCIA_MODIFY_MEMORY_WINDOW
author: windows-driver-content
description: The PCMCIA_MODIFY_MEMORY_WINDOW interface routine sets the attributes of a memory window for a PCMCIA memory card. The memory window is mapped by the PCMCIA bus driver.
old-location: pcmcia\pcmcia_modify_memory_window.htm
old-project: PCMCIA
ms.assetid: 01469cd7-a023-42b0-9306-fc390bf990e6
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: PARCLASS_NEGOTIATION_MASK, PARCLASS_NEGOTIATION_MASK, *PPARCLASS_NEGOTIATION_MASK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddpcm.h
req.include-header: Ntddpcm.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ModifyMemoryWindow
req.alt-loc: ntddpcm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL (See Remarks section.)
req.iface: 
---

# PCMCIA_MODIFY_MEMORY_WINDOW callback



## -description
<p>The <b>PCMCIA_MODIFY_MEMORY_WINDOW</b> interface routine sets the attributes of a memory window for a PCMCIA memory card. The memory window is mapped by the PCMCIA bus driver.</p>


## -prototype

````
PCMCIA_MODIFY_MEMORY_WINDOW ModifyMemoryWindow;

BOOLEAN ModifyMemoryWindow(
  _In_opt_ PVOID     Context,
  _In_     ULONGLONG HostBase,
  _In_     ULONGLONG CardBase,
  _In_     BOOLEAN   Enable,
  _In_opt_ ULONG     WindowSize,
  _In_opt_ UCHAR     AccessSpeed,
  _In_opt_ UCHAR     BusWidth,
  _In_opt_ BOOLEAN   AttributeMemory
)
{ ... }
````


## -parameters
<dl>

### -param Context [in, optional]

<dd>
<p>Pointer to the context for the interface routine.</p>
</dd>

### -param HostBase [in]

<dd>
<p>Specifies the physical memory window to map. <i>HostBase</i> is the base address for the memory card in the system's physical address space.</p>
</dd>

### -param CardBase [in]

<dd>
<p>Specifies the byte offset in the PC Card's or CardBus card's memory where the memory mapping begins.</p>
</dd>

### -param Enable [in]

<dd>
<p>Specifies permission to access the memory window. If <i>Enable</i> is <b>TRUE</b>, memory access is permitted, otherwise memory access is not permitted.</p>
</dd>

### -param WindowSize [in, optional]

<dd>
<p>Specifies the size, in bytes, of the memory window that is mapped. The value of <i>WindowSize</i> cannot exceed the memory window granted to the driver in its assigned resources. If the value of Enable is <b>TRUE</b> and the value of WindowSize is zero, the size of the memory window granted to the driver in its assigned resources is used. If <i>Enable</i> is <b>FALSE</b>, <i>WindowSize</i> is not used.</p>
</dd>

### -param AccessSpeed [in, optional]

<dd>
<p>Specifies the access speed of the PC Card or CardBus card. The value of <i>AccessSpeed</i> is encoded as specified by the <i>PC Card Standard, Release 6.1</i>. If Enable is <b>FALSE</b>, <i>AccessSpeed</i> is not used.</p>
</dd>

### -param BusWidth [in, optional]

<dd>
<p>Specifies the width of bus access to the PCMCIA memory card. <i>BusWidth</i> must be one of the following values:</p>
<p></p>
<dl>

### -param PCMCIA_MEMORY_8BIT_ACCESS

<dd></dd>
</dl>
<p>If <i>Enable</i> is <b>FALSE</b>, <i>BusWidth</i> is not used.</p>
</dd>

### -param AttributeMemory [in, optional]

<dd>
<p>Must be <b>FALSE</b> for common memory and <b>TRUE</b> for attribute memory. </p>
</dd>
</dl>

## -returns
<p>The <b>PCMCIA_MODIFY_MEMORY_WINDOW</b> interface routine returns <b>TRUE</b> if the memory window is successfully enabled or disabled, as specified by the <i>Enable</i> parameter.</p>

## -remarks
<p>A caller must set the <i>Context</i> parameter to the context that is specified by the PCMCIA bus driver. The PCMCIA bus driver returns the context for the interface routines in the <b>Context</b> member of the same PCMCIA_INTERFACE_STANDARD structure that contains the pointers to the interface routines. If the <i>Context</i> parameter is not valid, system behavior is not defined, and the system might halt.</p>

<p>Callers of this routine must be running at IRQL &lt;= DISPATCH_LEVEL. To maintain overall system performance, it is recommended that drivers call this routine at IRQL &lt; DISPATCH_LEVEL.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddpcm.h (include Ntddpcm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL (See Remarks section.)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537609">PCMCIA_IS_WRITE_PROTECTED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537611">PCMCIA_SET_VPP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCMCIA\buses]:%20PCMCIA_MODIFY_MEMORY_WINDOW callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
