---
UID: NC.wudfinterrupt.WUDF_INTERRUPT_DISABLE
title: WUDF_INTERRUPT_DISABLE
author: windows-driver-content
description: A driver's OnInterruptDisable event callback function disables a specified hardware interrupt.
old-location: wdf\oninterruptdisable.htm
old-project: wdf
ms.assetid: 3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: OnInterruptDisable
req.alt-loc: Wudfinterrupt.h
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

# WUDF_INTERRUPT_DISABLE callback



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver's <i>OnInterruptDisable</i> event callback function disables a specified hardware interrupt.



## -prototype

````
WUDF_INTERRUPT_DISABLE OnInterruptDisable;

HRESULT OnInterruptDisable(
  _In_ IWDFInterrupt *pInterrupt,
  _In_ IWDFDevice    *pAssociatedDevice
)
{ ... }
````


## -parameters

### -param pInterrupt [in]

A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfinterrupt.md">IWDFInterrupt</a> interface.


### -param pAssociatedDevice [in]

A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a> interface that the driver used to call <a href="wdf.iwdfdevice3_createinterrupt">CreateInterrupt</a>. 


## -returns
<i>OnInterruptDisable</i>  must return S_OK if the operation succeeds. Otherwise, the callback should return one of the error codes that are defined in Winerror.h.


## -remarks
To register an <i>OnInterruptDisable</i> callback function, your driver must place the callback function's address in a <a href="wdf.wudf_interrupt_config">WUDF_INTERRUPT_CONFIG</a> structure before calling <a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice::CreateInterrupt</a>.


The framework calls the driver's <i>OnInterruptDisable</i> callback function each time the device leaves its working (D0) state. Additionally, a driver can cause the framework to call the <i>OnInterruptDisable</i> callback function by calling <a href="wdf.iwdfinterrupt_disable">IWDFInterrupt::Disable</a>.


Before calling the <i>OnInterruptDisable</i> callback function, the framework calls the driver's <a href="wdf.ipnpcallbackhardwareinterrupt_ond0exitpreinterruptsdisabled">OnD0ExitPreInterruptsDisabled</a> event callback function and acquires the user-mode interrupt lock.


For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.

The function type is declared in <i>Wudfinterrupt.h</i>, as follows.

To define an <i>OnInterruptDisable</i> callback function that is named <i>MyInterruptDisable</i>, you must first provide a function declaration that SDV and other verification tools require, as follows:

Then, implement your callback function as follows:


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
<dt>Wudfinterrupt.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wudf_interrupt_config">WUDF_INTERRUPT_CONFIG</a>
</dt>
<dt>
<a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice::CreateInterrupt</a>
</dt>
<dt>
<a href="..\wudfinterrupt\nc-wudfinterrupt-wudf_interrupt_enable.md">OnInterruptEnable</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WUDF_INTERRUPT_DISABLE callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

