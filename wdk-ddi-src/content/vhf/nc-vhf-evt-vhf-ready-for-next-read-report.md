---
UID: NC.vhf.EVT_VHF_READY_FOR_NEXT_READ_REPORT
title: EVT_VHF_READY_FOR_NEXT_READ_REPORT
author: windows-driver-content
description: The HID source driver implements this event call back function to use its buffering scheme for HID Input Reports, and wants to get notified when the next report can be submitted to VHF.
old-location: hid\evtvhfreadyfornextreadreport.htm
old-project: hid
ms.assetid: 02DDBE00-C342-474B-8D06-FBB929BA4760
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR, USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR, *PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: vhf.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtVhfReadyForNextReadReport
req.alt-loc: vhf.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_VHF_READY_FOR_NEXT_READ_REPORT callback



## -description
<p>The HID source driver implements this event call back function to use its buffering scheme for HID Input Reports, and wants to get notified when the next report can be submitted to VHF.</p>


## -prototype

````
EVT_VHF_READY_FOR_NEXT_READ_REPORT EvtVhfReadyForNextReadReport;

void EvtVhfReadyForNextReadReport(
  _In_ PVOID VhfClientContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>VhfClientContext</i> [in]

<dd>
<p>Pointer to the HID source driver-defined context structure that the driver passed in the previous call to <a href="..\vhf\nf-vhf-vhfcreate.md">VhfCreate</a> to create the virtual HID device.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Virtual HID Framework (VHF) invokes this callback function to notify the HID source driver that it can submit a buffer to get the HID Input Report. After the callback is invoked, the HID source driver must call <a href="..\vhf\nf-vhf-vhfreadreportsubmit.md">VhfReadReportSubmit</a>  only once. If a portion of the HID Input Report is still pending, the driver must wait for VHF to invoke <i>EvtVhfReadyForNextReadReport</i> before the driver can call <b>VhfReadReportSubmit</b> again.</p>

<p>If the HID source driver does not implement this callback function, VHF uses a default buffering policy for HID Read (Input) Reports.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
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
<dt>Vhf.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Write a HID source driver by using Virtual HID Framework (VHF)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20EVT_VHF_READY_FOR_NEXT_READ_REPORT callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
