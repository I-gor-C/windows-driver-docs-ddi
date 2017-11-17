---
UID: NF.wudfddi.IWDFIoRequest3.SetActivityId
title: IWDFIoRequest3::SetActivityId
author: windows-driver-content
description: The SetActivityId method associates an activity identifier with an I/O request.
old-location: wdf\iwdfiorequest3_setactivityid.htm
ms.assetid: 57CB3CED-FE46-4A74-9E23-82640B7EF1DC
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFIoRequest3.SetActivityId
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
ms.keywords: IWDFIoRequest3, SetActivityId, IWDFIoRequest3::SetActivityId
req.iface: IWDFIoRequest3
req.product: Windows 10 or later.
---

# IWDFIoRequest3::SetActivityId method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
   The 
  <b>SetActivityId</b> method associates an activity identifier with an I/O request.</p>


## -syntax

````
void SetActivityId(
  [in] LPGUID ActivityId
);
````


## -parameters
<dl>

### -param <i>ActivityId</i> [in]

<dd>
<p>A pointer to the activity identifier GUID to store in the I/O request.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>Calling <b>SetActivityId</b> does not set an association with any previously present activity identifier. When the driver calls <b>SetActivityId</b>, any existing activity identifier is overwritten.</p>

<p>To set an association, retrieve the existing identifier by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451345">RetrieveActivityId</a> and then associate the existing identifier with the new one by calling <a href="etw.eventwritetransfer_func">EventWriteTransfer</a>.</p>

<p>The framework does not clear a request's activity identifier when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559048">IWdfIoRequest2::Reuse</a>.</p>

<p>For more information about activity identifiers, see <a href="wdf.using_activity_identifiers">Using Activity Identifiers</a>.</p>

<p>The UMDF 2 equivalent of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/dn265622">WdfRequestSetActivityId</a>.</p>

<p>For a code example that uses <b>SetActivityId</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451345">RetrieveActivityId</a>.</p>

<p>Calling <b>SetActivityId</b> does not set an association with any previously present activity identifier. When the driver calls <b>SetActivityId</b>, any existing activity identifier is overwritten.</p>

<p>To set an association, retrieve the existing identifier by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451345">RetrieveActivityId</a> and then associate the existing identifier with the new one by calling <a href="etw.eventwritetransfer_func">EventWriteTransfer</a>.</p>

<p>The framework does not clear a request's activity identifier when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559048">IWdfIoRequest2::Reuse</a>.</p>

<p>For more information about activity identifiers, see <a href="wdf.using_activity_identifiers">Using Activity Identifiers</a>.</p>

<p>The UMDF 2 equivalent of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/dn265622">WdfRequestSetActivityId</a>.</p>

<p>For a code example that uses <b>SetActivityId</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451345">RetrieveActivityId</a>.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8</p>
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
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451337">IWDFIoRequest3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/A90FCF3C-B648-4E97-887E-FCE58D7FA13A">IWDFIoRequest3::RetrieveActivityId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265622">WdfRequestSetActivityId</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest3::SetActivityId method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
