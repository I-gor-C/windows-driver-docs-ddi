---
UID: NS.wdm._SCATTER_GATHER_LIST~r2
title: SCATTER_GATHER_LIST
author: windows-driver-content
description: The SCATTER_GATHER_LIST structure describes the scatter/gather list for a DMA operation.
old-location: kernel\scatter_gather_list.htm
old-project: kernel
ms.assetid: 3cc6da15-8367-4430-afe8-956376eef1c7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SCATTER_GATHER_LIST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCATTER_GATHER_LIST
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# SCATTER_GATHER_LIST structure



## -description
<p>The <b>SCATTER_GATHER_LIST</b> structure describes the scatter/gather list for a DMA operation.</p>


## -syntax

````
typedef struct _SCATTER_GATHER_LIST {
  ULONG                  NumberOfElements;
  ULONG_PTR              Reserved;
  SCATTER_GATHER_ELEMENT Elements[];
} SCATTER_GATHER_LIST, *PSCATTER_GATHER_LIST;
````


## -struct-fields
<dl>

### -field NumberOfElements

<dd>
<p>Specifies the number of elements in the <b>Elements</b> array.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Elements

<dd>
<p>Specifies an array of scatter/gather elements that comprise a scatter/gather list. Each array element is a structure of type <b>SCATTER_GATHER_ELEMENT</b>, which is defined as follows:</p>
<pre class="syntax" xml:space="preserve"><code>typedef struct _SCATTER_GATHER_ELEMENT {
  PHYSICAL_ADDRESS  Address;
  ULONG  Length;
  ULONG_PTR  Reserved;
} SCATTER_GATHER_ELEMENT, *PSCATTER_GATHER_ELEMENT;</code></pre>
<p>The <b>SCATTER_GATHER_ELEMENT</b> structure specifies the length, in bytes, of a physically contiguous scatter/gather region and the starting physical address of this region.</p>
</dd>
</dl>

## -remarks
<p>For a driver that performs scatter/gather DMA, the <a href="kernel.getscattergatherlist">GetScatterGatherList</a> or <a href="kernel.buildscattergatherlist">BuildScatterGatherList</a> routine creates a scatter/gather list and passes this list to the driver's <a href="kernel.adapterlistcontrol">AdapterListControl</a> routine. This scatter/gather list consists of a <b>SCATTER_GATHER_LIST</b> structure that is immediately followed in memory by a <b>SCATTER_GATHER_ELEMENT</b> array. The number of elements in this array is specified by the <b>NumberOfElements</b> member of the <b>SCATTER_GATHER_LIST</b> structure.</p>

<p>For more information about scatter/gather lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565510">Using Scatter/Gather DMA</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.adapterlistcontrol">AdapterListControl</a>
</dt>
<dt>
<a href="kernel.buildscattergatherlist">BuildScatterGatherList</a>
</dt>
<dt>
<a href="kernel.getscattergatherlist">GetScatterGatherList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SCATTER_GATHER_LIST structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
