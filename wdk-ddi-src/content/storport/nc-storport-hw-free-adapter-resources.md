---
UID: NC.storport.HW_FREE_ADAPTER_RESOURCES
title: HW_FREE_ADAPTER_RESOURCES
author: windows-driver-content
description: The HwStorFreeAdapterResources callback routine allows the Storport virtual miniport driver to free resources when the virtual adapter is being removed. This is the last callback routine for the adapter.
old-location: storage\hwstorfreeadapterresources.htm
old-project: storage
ms.assetid: 2f12aab4-ca6e-473b-a342-2881c4a7b133
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwStorFreeAdapterResources
req.alt-loc: Storport.h
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
req.product: Windows 10 or later.
---

# HW_FREE_ADAPTER_RESOURCES callback



## -description
<p>The <b>HwStorFreeAdapterResources</b> callback routine allows the Storport virtual miniport driver to free resources when the virtual adapter is being removed. This is the last callback routine for the adapter.</p>


## -prototype

````
HW_FREE_ADAPTER_RESOURCES HwStorFreeAdapterResources;

VOID HwStorFreeAdapterResources(
   IN PVOID DeviceExtension
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceExtension</i> 

<dd>
<p>A pointer to the virtual miniport driver's per-adapter storage area.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The name <b>HwStorFreeAdapterResources</b> is  placeholder text for the actual routine name. The actual prototype of this routine is defined in Storport.h as follows:</p>

<p>The port driver calls the Storport virtual miniport's <b>HwStorFreeAdapterResources</b> at PASSIVE_LEVEL. </p>

<p>To define an <b>HwStorFreeAdapterResources</b> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p> For example, to define a <b>HwStorBuildIo</b><b>HwStorFreeAdapterResources</b>callback routine that is named <i>MyHwAdapterFreeResources</i>, use the <b>HW_FREE_ADAPTER_RESOURCES</b> type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The <b>HW_FREE_ADAPTER_RESOURCES</b> function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>HW_FREE_ADAPTER_RESOURCES</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/40BD11CD-A559-4F90-BF39-4ED2FB800392">Declaring Functions Using Function Role Types for Storport Drivers</a>. For information about _Use_decl_annotations_, see <a href="c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>The name <b>HwStorFreeAdapterResources</b> is  placeholder text for the actual routine name. The actual prototype of this routine is defined in Storport.h as follows:</p>

<p>The port driver calls the Storport virtual miniport's <b>HwStorFreeAdapterResources</b> at PASSIVE_LEVEL. </p>

<p>To define an <b>HwStorFreeAdapterResources</b> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p> For example, to define a <b>HwStorBuildIo</b><b>HwStorFreeAdapterResources</b>callback routine that is named <i>MyHwAdapterFreeResources</i>, use the <b>HW_FREE_ADAPTER_RESOURCES</b> type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The <b>HW_FREE_ADAPTER_RESOURCES</b> function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>HW_FREE_ADAPTER_RESOURCES</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/40BD11CD-A559-4F90-BF39-4ED2FB800392">Declaring Functions Using Function Role Types for Storport Drivers</a>. For information about _Use_decl_annotations_, see <a href="c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>