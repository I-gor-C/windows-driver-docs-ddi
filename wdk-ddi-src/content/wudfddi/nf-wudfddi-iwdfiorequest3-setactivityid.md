---
UID: NF.wudfddi.IWDFIoRequest3.SetActivityId
title: IWDFIoRequest3::SetActivityId method
author: windows-driver-content
description: The SetActivityId method associates an activity identifier with an I/O request.
old-location: wdf\iwdfiorequest3_setactivityid.htm
old-project: wdf
ms.assetid: 57CB3CED-FE46-4A74-9E23-82640B7EF1DC
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFIoRequest3, IWDFIoRequest3::SetActivityId, SetActivityId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFIoRequest3::SetActivityId method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


   The 
  <b>SetActivityId</b> method associates an activity identifier with an I/O request.



## -syntax

````
void SetActivityId(
  [in] LPGUID ActivityId
);
````


## -parameters

### -param ActivityId [in]

A pointer to the activity identifier GUID to store in the I/O request.


## -returns
This method does not return a value.


## -remarks
Calling <b>SetActivityId</b> does not set an association with any previously present activity identifier. When the driver calls <b>SetActivityId</b>, any existing activity identifier is overwritten.

To set an association, retrieve the existing identifier by calling <a href="wdf.iwdfiorequest3_retrieveactivityid">RetrieveActivityId</a> and then associate the existing identifier with the new one by calling <a href="etw.eventwritetransfer_func">EventWriteTransfer</a>.

The framework does not clear a request's activity identifier when the driver calls <a href="wdf.iwdfiorequest2_reuse">IWdfIoRequest2::Reuse</a>.

For more information about activity identifiers, see <a href="wdf.using_activity_identifiers">Using Activity Identifiers</a>.

The UMDF 2 equivalent of this method is <a href="wdf.wdfrequestsetactivityid">WdfRequestSetActivityId</a>.

For a code example that uses <b>SetActivityId</b>, see <a href="wdf.iwdfiorequest3_retrieveactivityid">RetrieveActivityId</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 8

</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.11

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest3.md">IWDFIoRequest3</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest3_retrieveactivityid">IWDFIoRequest3::RetrieveActivityId</a>
</dt>
<dt>
<a href="wdf.wdfrequestsetactivityid">WdfRequestSetActivityId</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest3::SetActivityId method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

