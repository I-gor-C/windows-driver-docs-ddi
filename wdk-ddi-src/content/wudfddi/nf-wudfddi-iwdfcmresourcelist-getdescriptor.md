---
UID: NF.wudfddi.IWDFCmResourceList.GetDescriptor
title: IWDFCmResourceList::GetDescriptor
author: windows-driver-content
description: The GetDescriptor method returns a pointer to a resource descriptor that is contained in this interface's resource list.
old-location: wdf\iwdfcmresourcelist_getdescriptor.htm
old-project: wdf
ms.assetid: 5E870D10-A03B-4CD8-A2DD-54A6AB527DB2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFCmResourceList, GetDescriptor, IWDFCmResourceList::GetDescriptor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFCmResourceList.GetDescriptor
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFCmResourceList
req.product: Windows 10 or later.
---

# IWDFCmResourceList::GetDescriptor method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
<p>The <b>GetDescriptor</b> method returns a pointer to a resource descriptor that is contained in this interface's resource list.</p>
</p>
<p>The <b>GetDescriptor</b> method returns a pointer to a resource descriptor that is contained in this interface's resource list.</p>


## -syntax

````
PCM_PARTIAL_RESOURCE_DESCRIPTOR GetDescriptor(
   ULONG Index
);
````


## -parameters
<dl>

### -param <i>Index</i> 

<dd>
<p>A zero-based index into the logical configuration that is contained in this interface's resource list.</p>
</dd>
</dl>

## -returns
<p><b>GetDescriptor</b> returns a pointer to a <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.</p>

## -remarks
<p>Drivers typically call <b>GetDescriptor</b> from within <a href="https://msdn.microsoft.com/library/windows/hardware/hh439734">OnPrepareHardware</a>, before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451225">MapIoSpace</a>.</p>

<p>The <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure  is defined in Wudfwdm.h.</p>

<p>For more information about parsing hardware resources, see <a href="wdf.finding_and_mapping_hardware_resources_in_a_umdf_driver">Finding and Mapping Hardware Resources in a UMDF Driver</a>.</p>

<p>See example code in <a href="wdf.iwdfdevice3_mapiospace">IWDFDevice3::MapIoSpace</a>.</p>

<p>Drivers typically call <b>GetDescriptor</b> from within <a href="https://msdn.microsoft.com/library/windows/hardware/hh439734">OnPrepareHardware</a>, before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451225">MapIoSpace</a>.</p>

<p>The <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure  is defined in Wudfwdm.h.</p>

<p>For more information about parsing hardware resources, see <a href="wdf.finding_and_mapping_hardware_resources_in_a_umdf_driver">Finding and Mapping Hardware Resources in a UMDF Driver</a>.</p>

<p>See example code in <a href="wdf.iwdfdevice3_mapiospace">IWDFDevice3::MapIoSpace</a>.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439762">IWDFCmResourceList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFCmResourceList::GetDescriptor method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
