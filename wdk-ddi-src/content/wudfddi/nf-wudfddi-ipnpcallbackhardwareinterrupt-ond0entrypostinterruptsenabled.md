---
UID: NF.wudfddi.IPnpCallbackHardwareInterrupt.OnD0EntryPostInterruptsEnabled
title: IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled method
author: windows-driver-content
description: A driver's OnD0EntryPostInterruptsEnabled event callback function performs device-specific operations that are required when the driver enables the device's hardware interrupts.
old-location: wdf\ipnpcallbackhardwareinterrupt_ond0entrypostinterruptsenabled.htm
old-project: wdf
ms.assetid: 6AA5AA6F-DC73-40E6-8EE0-CAA91D89A0E8
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IPnpCallbackHardwareInterrupt, IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled, OnD0EntryPostInterruptsEnabled
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IPnpCallbackHardwareInterrupt.OnD0EntryPostInterruptsEnabled
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
req.product: Windows 10 or later.
---

# IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver's <b>OnD0EntryPostInterruptsEnabled</b> event callback function performs device-specific operations that are required when the driver enables the device's hardware interrupts.



## -syntax

````
HRESULT OnD0EntryPostInterruptsEnabled(
  [in] IWDFDevice3            *pInterrupt,
  [in] WDF_POWER_DEVICE_STATE PreviousState
);
````


## -parameters

### -param pInterrupt [in]

A pointer to <a href="..\wudfddi\nn-wudfddi-iwdfdevice3.md">IWDFDevice3</a> interface.


### -param PreviousState [in]

A <a href="wdf.wdf_power_device_state">WDF_POWER_DEVICE_STATE</a>-typed enumerator that identifies the previous device power state.


## -returns
If successful, <b>OnD0EntryPostInterruptsEnabled</b> returns S_OK. Otherwise, it returns an appropriate failure status.


## -remarks
For more information, see <a href="wdf.enabling_and_disabling_interrupts_umdf">Enabling and Disabling Interrupts</a>.


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
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-ipnpcallbackhardwareinterrupt.md">IPnpCallbackHardwareInterrupt</a>
</dt>
<dt>
<a href="wdf.ipnpcallbackhardwareinterrupt_ond0exitpreinterruptsdisabled">OnD0ExitPreInterruptsDisabled</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
