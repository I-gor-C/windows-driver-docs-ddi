---
UID: NS.ntddk._WHEA_NOTIFICATION_DESCRIPTOR
title: WHEA_NOTIFICATION_DESCRIPTOR
author: windows-driver-content
description: The WHEA_NOTIFICATION_DESCRIPTOR structure describes the notification mechanism that is used by an error source.
old-location: whea\whea_notification_descriptor.htm
old-project: whea
ms.assetid: 5b228bb8-dd31-484d-b87a-ec7fed433a4a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_NOTIFICATION_DESCRIPTOR, WHEA_NOTIFICATION_DESCRIPTOR, *PWHEA_NOTIFICATION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_NOTIFICATION_DESCRIPTOR
req.alt-loc: Ntddk.h
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
req.iface: 
---

# WHEA_NOTIFICATION_DESCRIPTOR structure



## -description
<p>The <b>WHEA_NOTIFICATION_DESCRIPTOR</b> structure describes the notification mechanism that is used by an error source.</p>


## -syntax

````
struct WHEA_NOTIFICATION_DESCRIPTOR {
  UCHAR                   Type;
  UCHAR                   Length;
  WHEA_NOTIFICATION_FLAGS Flags;
  union {
    struct {
      ULONG PollInterval;
    } Polled;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } Interrupt;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } LocalInterrupt;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } Sci;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } Nmi;
  } u;
};
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of notification mechanism that is used by the error source. This can be one of the following possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT"></a><a id="whea_notification_type_externalinterrupt"></a><dl>

### -field <b>WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT</b>

</dl>
</td>
<td width="60%">
<p>The error source notifies the LLHEH for the error source by means of an external interrupt.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WHEA_NOTIFICATION_TYPE_LOCALINTERRUPT"></a><a id="whea_notification_type_localinterrupt"></a><dl>

### -field <b>WHEA_NOTIFICATION_TYPE_LOCALINTERRUPT</b>

</dl>
</td>
<td width="60%">
<p>The error source notifies the LLHEH for the error source by means of a local interrupt.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WHEA_NOTIFICATION_TYPE_NMI"></a><a id="whea_notification_type_nmi"></a><dl>

### -field <b>WHEA_NOTIFICATION_TYPE_NMI</b>

</dl>
</td>
<td width="60%">
<p>The error source notifies the LLHEH for the error source by means of a nonmaskable interrupt (NMI).</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WHEA_NOTIFICATION_TYPE_POLLED"></a><a id="whea_notification_type_polled"></a><dl>

### -field <b>WHEA_NOTIFICATION_TYPE_POLLED</b>

</dl>
</td>
<td width="60%">
<p>The low-level hardware error handler (LLHEH)for the error source must periodically poll the error status registers to check for an error condition.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WHEA_NOTIFICATION_TYPE_SCI"></a><a id="whea_notification_type_sci"></a><dl>

### -field <b>WHEA_NOTIFICATION_TYPE_SCI</b>

</dl>
</td>
<td width="60%">
<p>The error source notifies the LLHEH for the error source by means of a service control interrupt (SCI).</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Length</b>

<dd>
<p>The size, in bytes, of the <b>WHEA_NOTIFICATION_DESCRIPTOR</b> structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A WHEA_NOTIFICATION_FLAGS union that indicates which of the members of the <b>WHEA_NOTIFICATION_DESCRIPTOR</b> structure can be written to by the operating system. The WHEA_NOTIFICATION_FLAGS union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_NOTIFICATION_FLAGS {
  struct {
    USHORT  PollIntervalRW:1;
    USHORT  SwitchToPollingThresholdRW:1;
    USHORT  SwitchToPollingWindowRW:1;
    USHORT  ErrorThresholdRW:1;
    USHORT  ErrorThresholdWindowRW:1;
    USHORT  Reserved:11;
  };
  USHORT  AsUSHORT;
} WHEA_NOTIFICATION_FLAGS, *PWHEA_NOTIFICATION_FLAGS</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="AsUSHORT"></a><a id="asushort"></a><a id="ASUSHORT"></a><dl>

### -field <b><b>AsUSHORT</b></b>

</dl>
</td>
<td width="60%">
<p>A USHORT representation of the contents of the WHEA_NOTIFICATION_FLAGS union.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ErrorThresholdRW"></a><a id="errorthresholdrw"></a><a id="ERRORTHRESHOLDRW"></a><dl>

### -field <b><b>ErrorThresholdRW</b></b>

</dl>
</td>
<td width="60%">
<p>A single bit that indicates that the operating system can write to the <b>u.</b><i>xxx</i><b>.ErrorThreshold</b> members of the WHEA_NOTIFICATION_DESCRIPTOR structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="ErrorThresholdWindowRW"></a><a id="errorthresholdwindowrw"></a><a id="ERRORTHRESHOLDWINDOWRW"></a><dl>

### -field <b><b>ErrorThresholdWindowRW</b></b>

</dl>
</td>
<td width="60%">
<p>A single bit that indicates that the operating system can write to the <b>u.</b><i>xxx</i><b>.ErrorThresholdWindow</b> members of the WHEA_NOTIFICATION_DESCRIPTOR structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PollIntervalRW"></a><a id="pollintervalrw"></a><a id="POLLINTERVALRW"></a><dl>

### -field <b><b>PollIntervalRW</b></b>

</dl>
</td>
<td width="60%">
<p>A single bit that indicates that the operating system can write to the <b>u.</b><i>xxx</i><b>.PollInterval</b> members of the WHEA_NOTIFICATION_DESCRIPTOR structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><dl>

### -field <b><b>Reserved</b></b>

</dl>
</td>
<td width="60%">
<p>Reserved for system use.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SwitchToPollingThresholdRW"></a><a id="switchtopollingthresholdrw"></a><a id="SWITCHTOPOLLINGTHRESHOLDRW"></a><dl>

### -field <b><b>SwitchToPollingThresholdRW</b></b>

</dl>
</td>
<td width="60%">
<p>A single bit that indicates that the operating system can write to the <b>u.</b><i>xxx</i><b>.SwitchToPollingThreshold</b> members of the WHEA_NOTIFICATION_DESCRIPTOR structure.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SwitchToPollingWindowRW"></a><a id="switchtopollingwindowrw"></a><a id="SWITCHTOPOLLINGWINDOWRW"></a><dl>

### -field <b><b>SwitchToPollingWindowRW</b></b>

</dl>
</td>
<td width="60%">
<p>A single bit that indicates that the operating system can write to the <b>u.</b><i>xxx</i><b>.SwitchToPollingWindow</b> members of the WHEA_NOTIFICATION_DESCRIPTOR structure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>u</b>

<dd>
<p>A union of structures that are specific to each different type of notification mechanism. </p>
<dl>

### -field <b>Polled</b>

<dd>
<p>A structure that describes the notification mechanism when the <b>Type</b> member is set to WHEA_NOTIFICATION_TYPE_POLLED.</p>
<dl>

### -field <b>PollInterval</b>

<dd>
<p>The interval, in milliseconds, that the LLHEH for the error source should poll the error status registers to check for an error condition.</p>
</dd>
</dl>
</dd>

### -field <b>Interrupt</b>

<dd>
<p>A structure that describes the notification mechanism when the <b>Type</b> member is set to WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT.</p>
<dl>

### -field <b>PollInterval</b>

<dd>
<p>The interval, in milliseconds, that the LLHEH for the error source should poll the error status registers to check for an error condition if the error source is switched out of interrupt mode.</p>
</dd>

### -field <b>Vector</b>

<dd>
<p>The interrupt vector for the error source.</p>
</dd>

### -field <b>SwitchToPollingThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>SwitchToPollingWindow</b> member before the error source is switched to polling mode.</p>
</dd>

### -field <b>SwitchToPollingWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>SwitchToPollingThreshold</b> member must occur before the error source is switched to polling mode.</p>
</dd>

### -field <b>ErrorThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>ErrorThresholdWindow</b> member before an error from the error source is processed by the operating system.</p>
</dd>

### -field <b>ErrorThresholdWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>ErrorThreshold</b> member must occur before an error from the error source is processed by the operating system.</p>
</dd>
</dl>
</dd>

### -field <b>LocalInterrupt</b>

<dd>
<p>A structure that describes the notification mechanism when the <b>Type</b> member is set to WHEA_NOTIFICATION_TYPE_LOCALINTERRUPT.</p>
<dl>

### -field <b>PollInterval</b>

<dd>
<p>The interval, in milliseconds, that the LLHEH for the error source should poll the error status registers to check for an error condition if the error source is switched out of interrupt mode.</p>
</dd>

### -field <b>Vector</b>

<dd>
<p>The interrupt vector for the error source.</p>
</dd>

### -field <b>SwitchToPollingThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>SwitchToPollingWindow</b> member before the error source is switched to polling mode.</p>
</dd>

### -field <b>SwitchToPollingWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>SwitchToPollingThreshold</b> member must occur before the error source is switched to polling mode.</p>
</dd>

### -field <b>ErrorThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>ErrorThresholdWindow</b> member before an error from the error source is processed by the operating system.</p>
</dd>

### -field <b>ErrorThresholdWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>ErrorThreshold</b> member must occur before an error from the error source is processed by the operating system.</p>
</dd>
</dl>
</dd>

### -field <b>Sci</b>

<dd>
<p> A structure that describes the notification mechanism when the <b>Type</b> member is set to WHEA_NOTIFICATION_TYPE_SCI.</p>
<dl>

### -field <b>PollInterval</b>

<dd>
<p>The interval, in milliseconds, that the LLHEH for the error source should poll the error status registers to check for an error condition if the error source is switched out of interrupt mode.</p>
</dd>

### -field <b>Vector</b>

<dd>
<p>The interrupt vector for the error source.</p>
</dd>

### -field <b>SwitchToPollingThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>SwitchToPollingWindow</b> member before the error source is switched to polling mode.</p>
</dd>

### -field <b>SwitchToPollingWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>SwitchToPollingThreshold</b> member must occur before the error source is switched to polling mode.</p>
</dd>

### -field <b>ErrorThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>ErrorThresholdWindow</b> member before an error from the error source is processed by the operating system.</p>
</dd>

### -field <b>ErrorThresholdWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>ErrorThreshold</b> member must occur before an error from the error source is processed by the operating system.</p>
</dd>
</dl>
</dd>

### -field <b>Nmi</b>

<dd>
<p>A structure that describes the notification mechanism when the <b>Type</b> member is set to WHEA_NOTIFICATION_TYPE_NMI.</p>
<dl>

### -field <b>PollInterval</b>

<dd>
<p>The interval, in milliseconds, that the LLHEH for the error source should poll the error status registers to check for an error condition if the error source is switched out of interrupt mode.</p>
</dd>

### -field <b>Vector</b>

<dd>
<p>The interrupt vector for the error source.</p>
</dd>

### -field <b>SwitchToPollingThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>SwitchToPollingWindow</b> member before the error source is switched to polling mode.</p>
</dd>

### -field <b>SwitchToPollingWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>SwitchToPollingThreshold</b> member must occur before the error source is switched to polling mode.</p>
</dd>

### -field <b>ErrorThreshold</b>

<dd>
<p>The number of errors that must occur within the time specified by the <b>ErrorThresholdWindow</b> member before an error from the error source is processed by the operating system.</p>
</dd>

### -field <b>ErrorThresholdWindow</b>

<dd>
<p>The window of time, in seconds, in which the number of errors specified by the <b>ErrorThreshold</b> member must occur before an error from the error source is processed by the operating system.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A WHEA_NOTIFICATION_DESCRIPTOR structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560531">WHEA_GENERIC_ERROR_DESCRIPTOR</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560646">WHEA_XPF_CMC_DESCRIPTOR</a> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560531">WHEA_GENERIC_ERROR_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560646">WHEA_XPF_CMC_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_NOTIFICATION_DESCRIPTOR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
