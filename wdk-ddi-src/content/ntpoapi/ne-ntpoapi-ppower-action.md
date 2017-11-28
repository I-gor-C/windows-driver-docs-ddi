---
UID: NE.ntpoapi.PPOWER_ACTION
title: PPOWER_ACTION
author: windows-driver-content
description: The POWER_ACTION enumeration identifies the system power actions that can occur on a computer.
old-location: wdf\power_action.htm
old-project: wdf
ms.assetid: 0c4a5eb8-d364-4e5d-9d2f-2605c8c34f63
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NLSTABLEINFO, NLSTABLEINFO, *PNLSTABLEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntpoapi.h
req.include-header: Wudfddi.h, Ntpoapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: POWER_ACTION
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PPOWER_ACTION enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>POWER_ACTION</b> enumeration identifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564553">system power actions</a> that can occur on a computer.</p>


## -syntax

````
typedef enum  { 
  PowerActionNone           = 0,
  PowerActionReserved       = ( PowerActionNone + 1 ),
  PowerActionSleep          = ( PowerActionReserved + 1 ),
  PowerActionHibernate      = ( PowerActionSleep + 1 ),
  PowerActionShutdown       = ( PowerActionHibernate + 1 ),
  PowerActionShutdownReset  = ( PowerActionShutdown + 1 ),
  PowerActionShutdownOff    = ( PowerActionShutdownReset + 1 ),
  PowerActionWarmEject      = ( PowerActionShutdownOff + 1 )
} POWER_ACTION, *PPOWER_ACTION;
````


## -enum-fields
<dl>

### -field <a id="PowerActionNone"></a><a id="poweractionnone"></a><a id="POWERACTIONNONE"></a><b>PowerActionNone</b>

<dd>
<p>No power action is taking place.</p>
</dd>

### -field <a id="PowerActionReserved"></a><a id="poweractionreserved"></a><a id="POWERACTIONRESERVED"></a><b>PowerActionReserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="PowerActionSleep"></a><a id="poweractionsleep"></a><a id="POWERACTIONSLEEP"></a><b>PowerActionSleep</b>

<dd>
<p>The computer is entering a <a href="https://msdn.microsoft.com/2fd883b5-4e89-4ce9-b75a-b821348ac860">system sleeping (S1, S2, or S3) state</a>.</p>
</dd>

### -field <a id="PowerActionHibernate"></a><a id="poweractionhibernate"></a><a id="POWERACTIONHIBERNATE"></a><b>PowerActionHibernate</b>

<dd>
<p>The computer is entering its <a href="https://msdn.microsoft.com/2fd883b5-4e89-4ce9-b75a-b821348ac860">hibernation (S4) state</a>.</p>
</dd>

### -field <a id="PowerActionShutdown"></a><a id="poweractionshutdown"></a><a id="POWERACTIONSHUTDOWN"></a><b>PowerActionShutdown</b>

<dd>
<p>The computer is entering its <a href="https://msdn.microsoft.com/c08d688d-c31a-4d57-a343-406edfa35e8f">shutdown (S5) state</a>. After all devices have entered their <a href="https://msdn.microsoft.com/f594a63f-10ce-439d-abe3-d342555d98f0">off (D3) state</a>, the computer remains powered on until an administrator presses the power button.</p>
</dd>

### -field <a id="PowerActionShutdownReset"></a><a id="poweractionshutdownreset"></a><a id="POWERACTIONSHUTDOWNRESET"></a><b>PowerActionShutdownReset</b>

<dd>
<p>The computer is entering its shutdown (S5) state. After all devices have entered their off (D3) state, the computer automatically powers off and then immediately restarts and returns to its working (S0) state.</p>
</dd>

### -field <a id="PowerActionShutdownOff"></a><a id="poweractionshutdownoff"></a><a id="POWERACTIONSHUTDOWNOFF"></a><b>PowerActionShutdownOff</b>

<dd>
<p>The computer is entering its shutdown (S5) state. After all devices have entered their off (D3) state, the computer automatically powers off.</p>
</dd>

### -field <a id="PowerActionWarmEject"></a><a id="poweractionwarmeject"></a><a id="POWERACTIONWARMEJECT"></a><b>PowerActionWarmEject</b>

<dd>
<p>The computer is being ejected from an ACPI-compatible dock device. Typically, the computer's power state does not change.</p>
</dd>
</dl>

## -remarks
<p>The <b>POWER_ACTION</b> enumeration is used as the return value for <a href="https://msdn.microsoft.com/library/windows/hardware/ff556936">IWDFDevice2::GetSystemPowerAction</a>.</p>

<p>The <b>POWER_ACTION</b> enumeration is used as the return value for <a href="https://msdn.microsoft.com/library/windows/hardware/ff556936">IWDFDevice2::GetSystemPowerAction</a>.</p>

<p>The <b>POWER_ACTION</b> enumeration is used as the return value for <a href="https://msdn.microsoft.com/library/windows/hardware/ff556936">IWDFDevice2::GetSystemPowerAction</a>.</p>

## -requirements
<table>
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
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h or Ntpoapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556936">IWDFDevice2::GetSystemPowerAction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20POWER_ACTION enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
