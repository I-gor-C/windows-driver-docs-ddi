---
UID: NF.wudfddi.IWDFDevice3.UnmapIoSpace
title: IWDFDevice3::UnmapIoSpace
author: windows-driver-content
description: The UnmapIoSpace method unmaps a specified range of physical addresses previously mapped by MapIoSpace method.
old-location: wdf\iwdfdevice3_unmapiospace.htm
old-project: wdf
ms.assetid: E95AC8E6-222A-4C88-8EBD-6BD7F22B9F18
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFDevice3, UnmapIoSpace, IWDFDevice3::UnmapIoSpace
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
req.alt-api: IWDFDevice3.UnmapIoSpace
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
req.iface: IWDFDevice3
req.product: Windows 10 or later.
---

# IWDFDevice3::UnmapIoSpace method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>UnmapIoSpace</b> method unmaps a specified range of physical addresses previously mapped by <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method.</p>


## -syntax

````
VOID UnmapIoSpace(
  [in] PVOID  *PseudoBaseAddress,
  [in] SIZE_T NumberOfBytes
);
````


## -parameters
<dl>

### -param PseudoBaseAddress [in]

<dd>
<p>Pointer to the pseudo base address obtained from a previous call to <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method to which the physical address range was mapped.</p>
</dd>

### -param NumberOfBytes [in]

<dd>
<p>Specifies the number of bytes that were mapped.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>If a driver calls <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> in <a href="wdf.ipnpcallbackhardware2_onpreparehardware">OnPrepareHardware</a> callback. It calls <b>UnmapIoSpace</b> in its <a href="wdf.ipnpcallbackhardware2_onreleasehardware">OnReleaseHardware</a> callback.</p>

<p>For an example, see <a href="wdf.finding_and_mapping_hardware_resources_in_a_umdf_driver">Finding and Mapping Hardware Resources in a UMDF Driver</a>.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfdevice3.md">IWDFDevice3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice3::UnmapIoSpace method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
