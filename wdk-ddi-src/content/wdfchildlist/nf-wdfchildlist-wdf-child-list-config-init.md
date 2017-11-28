---
UID: NF.wdfchildlist.WDF_CHILD_LIST_CONFIG_INIT
title: WDF_CHILD_LIST_CONFIG_INIT
author: windows-driver-content
description: The WDF_CHILD_LIST_CONFIG_INIT function initializes a WDF_CHILD_LIST_CONFIG structure.
old-location: wdf\wdf_child_list_config_init.htm
old-project: wdf
ms.assetid: d222f2f3-554f-43d5-97c5-9a56fdb42ec3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_CHILD_LIST_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_LIST_CONFIG_INIT
req.alt-loc: wdfchildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_LIST_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_CHILD_LIST_CONFIG_INIT</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551227">WDF_CHILD_LIST_CONFIG</a> structure.</p>


## -syntax

````
VOID WDF_CHILD_LIST_CONFIG_INIT(
  _Out_ PWDF_CHILD_LIST_CONFIG           Config,
  _In_  ULONG                            IdentificationDescriptionSize,
  _In_  PFN_WDF_CHILD_LIST_CREATE_DEVICE EvtChildListCreateDevice
);
````


## -parameters
<dl>

### -param <i>Config</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551227">WDF_CHILD_LIST_CONFIG</a> structure.</p>
</dd>

### -param <i>IdentificationDescriptionSize</i> [in]

<dd>
<p>The size, in bytes, of each child device's <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a>. </p>
</dd>

### -param <i>EvtChildListCreateDevice</i> [in]

<dd>
<p>The address of a driver-supplied <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a> event callback function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_CHILD_LIST_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551227">WDF_CHILD_LIST_CONFIG</a> structure and sets the structure's <b>Size</b> member. Then it sets the <b>IdentificationDescriptionSize</b> and <b>EvtChildListCreateDevice</b> members to the specified values.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WDF_CHILD_LIST_CONFIG_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>.</p>

<p>The <b>WDF_CHILD_LIST_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551227">WDF_CHILD_LIST_CONFIG</a> structure and sets the structure's <b>Size</b> member. Then it sets the <b>IdentificationDescriptionSize</b> and <b>EvtChildListCreateDevice</b> members to the specified values.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WDF_CHILD_LIST_CONFIG_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551227">WDF_CHILD_LIST_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_LIST_CONFIG_INIT function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
