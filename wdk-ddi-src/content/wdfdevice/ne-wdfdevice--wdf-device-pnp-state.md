---
UID: NE.wdfdevice._WDF_DEVICE_PNP_STATE
title: WDF_DEVICE_PNP_STATE
author: windows-driver-content
description: The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter.
old-location: wdf\wdf_device_pnp_state.htm
ms.assetid: b907a1ca-d9ef-45e9-9e1b-26e58e3e1e07
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_DEVICE_PNP_STATE
req.alt-loc: wdfdevice.h
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
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_PNP_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter.</p>


## -syntax

````
typedef enum _WDF_DEVICE_PNP_STATE { 
  WdfDevStatePnpInvalid                             = 0x00,
  WdfDevStatePnpObjectCreated                       = 0x100,
  WdfDevStatePnpCheckForDevicePresence              = 0x101,
  WdfDevStatePnpEjectFailed                         = 0x102,
  WdfDevStatePnpEjectHardware                       = 0x103,
  WdfDevStatePnpEjectedWaitingForRemove             = 0x104,
  WdfDevStatePnpInit                                = 0x105,
  WdfDevStatePnpInitStarting                        = 0x106,
  WdfDevStatePnpInitSurpriseRemoved                 = 0x107,
  WdfDevStatePnpHardwareAvailable                   = 0x108,
  WdfDevStatePnpEnableInterfaces                    = 0x109,
  WdfDevStatePnpHardwareAvailablePowerPolicyFailed  = 0x10A,
  WdfDevStatePnpQueryRemoveAskDriver                = 0x10B,
  WdfDevStatePnpQueryRemovePending                  = 0x10C,
  WdfDevStatePnpQueryRemoveStaticCheck              = 0x10D,
  WdfDevStatePnpQueriedRemoving                     = 0x10E,
  WdfDevStatePnpQueryStopAskDriver                  = 0x10F,
  WdfDevStatePnpQueryStopPending                    = 0x110,
  WdfDevStatePnpQueryStopStaticCheck                = 0x111,
  WdfDevStatePnpQueryCanceled                       = 0x112,
  WdfDevStatePnpRemoved                             = 0x113,
  WdfDevStatePnpPdoRemoved                          = 0x114,
  WdfDevStatePnpRemovedPdoWait                      = 0x115,
  WdfDevStatePnpRemovedPdoSurpriseRemoved           = 0x116,
  WdfDevStatePnpRemovingDisableInterfaces           = 0x117,
  WdfDevStatePnpRestarting                          = 0x118,
  WdfDevStatePnpStarted                             = 0x119,
  WdfDevStatePnpStartedCancelStop                   = 0x11A,
  WdfDevStatePnpStartedCancelRemove                 = 0x11B,
  WdfDevStatePnpStartedRemoving                     = 0x11C,
  WdfDevStatePnpStartingFromStopped                 = 0x11D,
  WdfDevStatePnpStopped                             = 0x11E,
  WdfDevStatePnpStoppedWaitForStartCompletion       = 0x11F,
  WdfDevStatePnpStartedStopping                     = 0x120,
  WdfDevStatePnpSurpriseRemove                      = 0x121,
  WdfDevStatePnpInitQueryRemove                     = 0x122,
  WdfDevStatePnpInitQueryRemoveCanceled             = 0x123,
  WdfDevStatePnpFdoRemoved                          = 0x124,
  WdfDevStatePnpRemovedWaitForChildren              = 0x125,
  WdfDevStatePnpQueriedSurpriseRemove               = 0x126,
  WdfDevStatePnpSurpriseRemoveIoStarted             = 0x127,
  WdfDevStatePnpFailedPowerDown                     = 0x128,
  WdfDevStatePnpFailedIoStarting                    = 0x129,
  WdfDevStatePnpFailedOwnHardware                   = 0x12A,
  WdfDevStatePnpFailed                              = 0x12B,
  WdfDevStatePnpFailedSurpriseRemoved               = 0x12C,
  WdfDevStatePnpFailedStarted                       = 0x12D,
  WdfDevStatePnpFailedWaitForRemove                 = 0x12E,
  WdfDevStatePnpFailedInit                          = 0x12F,
  WdfDevStatePnpPdoInitFailed                       = 0x130,
  WdfDevStatePnpRestart                             = 0x131,
  WdfDevStatePnpRestartReleaseHardware              = 0x132,
  WdfDevStatePnpRestartHardwareAvailable            = 0x133,
  WdfDevStatePnpPdoRestart                          = 0x134,
  WdfDevStatePnpFinal                               = 0x135,
  WdfDevStatePnpRemovedChildrenRemoved              = 0x136,
  WdfDevStatePnpQueryRemoveEnsureDeviceAwake        = 0x137,
  WdfDevStatePnpQueryStopEnsureDeviceAwake          = 0x138,
  WdfDevStatePnpFailedPowerPolicyRemoved            = 0x139,
  WdfDevStatePnpNull                                = 0x13A
} WDF_DEVICE_PNP_STATE, *PWDF_DEVICE_PNP_STATE;
````


## -enum-fields
<dl>

### -field <a id="WdfDevStatePnpInvalid"></a><a id="wdfdevstatepnpinvalid"></a><a id="WDFDEVSTATEPNPINVALID"></a><b>WdfDevStatePnpInvalid</b>

<dd></dd>

### -field <a id="WdfDevStatePnpObjectCreated"></a><a id="wdfdevstatepnpobjectcreated"></a><a id="WDFDEVSTATEPNPOBJECTCREATED"></a><b>WdfDevStatePnpObjectCreated</b>

<dd></dd>

### -field <a id="WdfDevStatePnpCheckForDevicePresence"></a><a id="wdfdevstatepnpcheckfordevicepresence"></a><a id="WDFDEVSTATEPNPCHECKFORDEVICEPRESENCE"></a><b>WdfDevStatePnpCheckForDevicePresence</b>

<dd></dd>

### -field <a id="WdfDevStatePnpEjectFailed"></a><a id="wdfdevstatepnpejectfailed"></a><a id="WDFDEVSTATEPNPEJECTFAILED"></a><b>WdfDevStatePnpEjectFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePnpEjectHardware"></a><a id="wdfdevstatepnpejecthardware"></a><a id="WDFDEVSTATEPNPEJECTHARDWARE"></a><b>WdfDevStatePnpEjectHardware</b>

<dd></dd>

### -field <a id="WdfDevStatePnpEjectedWaitingForRemove"></a><a id="wdfdevstatepnpejectedwaitingforremove"></a><a id="WDFDEVSTATEPNPEJECTEDWAITINGFORREMOVE"></a><b>WdfDevStatePnpEjectedWaitingForRemove</b>

<dd></dd>

### -field <a id="WdfDevStatePnpInit"></a><a id="wdfdevstatepnpinit"></a><a id="WDFDEVSTATEPNPINIT"></a><b>WdfDevStatePnpInit</b>

<dd></dd>

### -field <a id="WdfDevStatePnpInitStarting"></a><a id="wdfdevstatepnpinitstarting"></a><a id="WDFDEVSTATEPNPINITSTARTING"></a><b>WdfDevStatePnpInitStarting</b>

<dd></dd>

### -field <a id="WdfDevStatePnpInitSurpriseRemoved"></a><a id="wdfdevstatepnpinitsurpriseremoved"></a><a id="WDFDEVSTATEPNPINITSURPRISEREMOVED"></a><b>WdfDevStatePnpInitSurpriseRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpHardwareAvailable"></a><a id="wdfdevstatepnphardwareavailable"></a><a id="WDFDEVSTATEPNPHARDWAREAVAILABLE"></a><b>WdfDevStatePnpHardwareAvailable</b>

<dd></dd>

### -field <a id="WdfDevStatePnpEnableInterfaces"></a><a id="wdfdevstatepnpenableinterfaces"></a><a id="WDFDEVSTATEPNPENABLEINTERFACES"></a><b>WdfDevStatePnpEnableInterfaces</b>

<dd></dd>

### -field <a id="WdfDevStatePnpHardwareAvailablePowerPolicyFailed"></a><a id="wdfdevstatepnphardwareavailablepowerpolicyfailed"></a><a id="WDFDEVSTATEPNPHARDWAREAVAILABLEPOWERPOLICYFAILED"></a><b>WdfDevStatePnpHardwareAvailablePowerPolicyFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryRemoveAskDriver"></a><a id="wdfdevstatepnpqueryremoveaskdriver"></a><a id="WDFDEVSTATEPNPQUERYREMOVEASKDRIVER"></a><b>WdfDevStatePnpQueryRemoveAskDriver</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryRemovePending"></a><a id="wdfdevstatepnpqueryremovepending"></a><a id="WDFDEVSTATEPNPQUERYREMOVEPENDING"></a><b>WdfDevStatePnpQueryRemovePending</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryRemoveStaticCheck"></a><a id="wdfdevstatepnpqueryremovestaticcheck"></a><a id="WDFDEVSTATEPNPQUERYREMOVESTATICCHECK"></a><b>WdfDevStatePnpQueryRemoveStaticCheck</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueriedRemoving"></a><a id="wdfdevstatepnpqueriedremoving"></a><a id="WDFDEVSTATEPNPQUERIEDREMOVING"></a><b>WdfDevStatePnpQueriedRemoving</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryStopAskDriver"></a><a id="wdfdevstatepnpquerystopaskdriver"></a><a id="WDFDEVSTATEPNPQUERYSTOPASKDRIVER"></a><b>WdfDevStatePnpQueryStopAskDriver</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryStopPending"></a><a id="wdfdevstatepnpquerystoppending"></a><a id="WDFDEVSTATEPNPQUERYSTOPPENDING"></a><b>WdfDevStatePnpQueryStopPending</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryStopStaticCheck"></a><a id="wdfdevstatepnpquerystopstaticcheck"></a><a id="WDFDEVSTATEPNPQUERYSTOPSTATICCHECK"></a><b>WdfDevStatePnpQueryStopStaticCheck</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryCanceled"></a><a id="wdfdevstatepnpquerycanceled"></a><a id="WDFDEVSTATEPNPQUERYCANCELED"></a><b>WdfDevStatePnpQueryCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRemoved"></a><a id="wdfdevstatepnpremoved"></a><a id="WDFDEVSTATEPNPREMOVED"></a><b>WdfDevStatePnpRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpPdoRemoved"></a><a id="wdfdevstatepnppdoremoved"></a><a id="WDFDEVSTATEPNPPDOREMOVED"></a><b>WdfDevStatePnpPdoRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRemovedPdoWait"></a><a id="wdfdevstatepnpremovedpdowait"></a><a id="WDFDEVSTATEPNPREMOVEDPDOWAIT"></a><b>WdfDevStatePnpRemovedPdoWait</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRemovedPdoSurpriseRemoved"></a><a id="wdfdevstatepnpremovedpdosurpriseremoved"></a><a id="WDFDEVSTATEPNPREMOVEDPDOSURPRISEREMOVED"></a><b>WdfDevStatePnpRemovedPdoSurpriseRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRemovingDisableInterfaces"></a><a id="wdfdevstatepnpremovingdisableinterfaces"></a><a id="WDFDEVSTATEPNPREMOVINGDISABLEINTERFACES"></a><b>WdfDevStatePnpRemovingDisableInterfaces</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRestarting"></a><a id="wdfdevstatepnprestarting"></a><a id="WDFDEVSTATEPNPRESTARTING"></a><b>WdfDevStatePnpRestarting</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStarted"></a><a id="wdfdevstatepnpstarted"></a><a id="WDFDEVSTATEPNPSTARTED"></a><b>WdfDevStatePnpStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStartedCancelStop"></a><a id="wdfdevstatepnpstartedcancelstop"></a><a id="WDFDEVSTATEPNPSTARTEDCANCELSTOP"></a><b>WdfDevStatePnpStartedCancelStop</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStartedCancelRemove"></a><a id="wdfdevstatepnpstartedcancelremove"></a><a id="WDFDEVSTATEPNPSTARTEDCANCELREMOVE"></a><b>WdfDevStatePnpStartedCancelRemove</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStartedRemoving"></a><a id="wdfdevstatepnpstartedremoving"></a><a id="WDFDEVSTATEPNPSTARTEDREMOVING"></a><b>WdfDevStatePnpStartedRemoving</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStartingFromStopped"></a><a id="wdfdevstatepnpstartingfromstopped"></a><a id="WDFDEVSTATEPNPSTARTINGFROMSTOPPED"></a><b>WdfDevStatePnpStartingFromStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStopped"></a><a id="wdfdevstatepnpstopped"></a><a id="WDFDEVSTATEPNPSTOPPED"></a><b>WdfDevStatePnpStopped</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStoppedWaitForStartCompletion"></a><a id="wdfdevstatepnpstoppedwaitforstartcompletion"></a><a id="WDFDEVSTATEPNPSTOPPEDWAITFORSTARTCOMPLETION"></a><b>WdfDevStatePnpStoppedWaitForStartCompletion</b>

<dd></dd>

### -field <a id="WdfDevStatePnpStartedStopping"></a><a id="wdfdevstatepnpstartedstopping"></a><a id="WDFDEVSTATEPNPSTARTEDSTOPPING"></a><b>WdfDevStatePnpStartedStopping</b>

<dd></dd>

### -field <a id="WdfDevStatePnpSurpriseRemove"></a><a id="wdfdevstatepnpsurpriseremove"></a><a id="WDFDEVSTATEPNPSURPRISEREMOVE"></a><b>WdfDevStatePnpSurpriseRemove</b>

<dd></dd>

### -field <a id="WdfDevStatePnpInitQueryRemove"></a><a id="wdfdevstatepnpinitqueryremove"></a><a id="WDFDEVSTATEPNPINITQUERYREMOVE"></a><b>WdfDevStatePnpInitQueryRemove</b>

<dd></dd>

### -field <a id="WdfDevStatePnpInitQueryRemoveCanceled"></a><a id="wdfdevstatepnpinitqueryremovecanceled"></a><a id="WDFDEVSTATEPNPINITQUERYREMOVECANCELED"></a><b>WdfDevStatePnpInitQueryRemoveCanceled</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFdoRemoved"></a><a id="wdfdevstatepnpfdoremoved"></a><a id="WDFDEVSTATEPNPFDOREMOVED"></a><b>WdfDevStatePnpFdoRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRemovedWaitForChildren"></a><a id="wdfdevstatepnpremovedwaitforchildren"></a><a id="WDFDEVSTATEPNPREMOVEDWAITFORCHILDREN"></a><b>WdfDevStatePnpRemovedWaitForChildren</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueriedSurpriseRemove"></a><a id="wdfdevstatepnpqueriedsurpriseremove"></a><a id="WDFDEVSTATEPNPQUERIEDSURPRISEREMOVE"></a><b>WdfDevStatePnpQueriedSurpriseRemove</b>

<dd></dd>

### -field <a id="WdfDevStatePnpSurpriseRemoveIoStarted"></a><a id="wdfdevstatepnpsurpriseremoveiostarted"></a><a id="WDFDEVSTATEPNPSURPRISEREMOVEIOSTARTED"></a><b>WdfDevStatePnpSurpriseRemoveIoStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedPowerDown"></a><a id="wdfdevstatepnpfailedpowerdown"></a><a id="WDFDEVSTATEPNPFAILEDPOWERDOWN"></a><b>WdfDevStatePnpFailedPowerDown</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedIoStarting"></a><a id="wdfdevstatepnpfailediostarting"></a><a id="WDFDEVSTATEPNPFAILEDIOSTARTING"></a><b>WdfDevStatePnpFailedIoStarting</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedOwnHardware"></a><a id="wdfdevstatepnpfailedownhardware"></a><a id="WDFDEVSTATEPNPFAILEDOWNHARDWARE"></a><b>WdfDevStatePnpFailedOwnHardware</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailed"></a><a id="wdfdevstatepnpfailed"></a><a id="WDFDEVSTATEPNPFAILED"></a><b>WdfDevStatePnpFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedSurpriseRemoved"></a><a id="wdfdevstatepnpfailedsurpriseremoved"></a><a id="WDFDEVSTATEPNPFAILEDSURPRISEREMOVED"></a><b>WdfDevStatePnpFailedSurpriseRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedStarted"></a><a id="wdfdevstatepnpfailedstarted"></a><a id="WDFDEVSTATEPNPFAILEDSTARTED"></a><b>WdfDevStatePnpFailedStarted</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedWaitForRemove"></a><a id="wdfdevstatepnpfailedwaitforremove"></a><a id="WDFDEVSTATEPNPFAILEDWAITFORREMOVE"></a><b>WdfDevStatePnpFailedWaitForRemove</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedInit"></a><a id="wdfdevstatepnpfailedinit"></a><a id="WDFDEVSTATEPNPFAILEDINIT"></a><b>WdfDevStatePnpFailedInit</b>

<dd></dd>

### -field <a id="WdfDevStatePnpPdoInitFailed"></a><a id="wdfdevstatepnppdoinitfailed"></a><a id="WDFDEVSTATEPNPPDOINITFAILED"></a><b>WdfDevStatePnpPdoInitFailed</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRestart"></a><a id="wdfdevstatepnprestart"></a><a id="WDFDEVSTATEPNPRESTART"></a><b>WdfDevStatePnpRestart</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRestartReleaseHardware"></a><a id="wdfdevstatepnprestartreleasehardware"></a><a id="WDFDEVSTATEPNPRESTARTRELEASEHARDWARE"></a><b>WdfDevStatePnpRestartReleaseHardware</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRestartHardwareAvailable"></a><a id="wdfdevstatepnprestarthardwareavailable"></a><a id="WDFDEVSTATEPNPRESTARTHARDWAREAVAILABLE"></a><b>WdfDevStatePnpRestartHardwareAvailable</b>

<dd></dd>

### -field <a id="WdfDevStatePnpPdoRestart"></a><a id="wdfdevstatepnppdorestart"></a><a id="WDFDEVSTATEPNPPDORESTART"></a><b>WdfDevStatePnpPdoRestart</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFinal"></a><a id="wdfdevstatepnpfinal"></a><a id="WDFDEVSTATEPNPFINAL"></a><b>WdfDevStatePnpFinal</b>

<dd></dd>

### -field <a id="WdfDevStatePnpRemovedChildrenRemoved"></a><a id="wdfdevstatepnpremovedchildrenremoved"></a><a id="WDFDEVSTATEPNPREMOVEDCHILDRENREMOVED"></a><b>WdfDevStatePnpRemovedChildrenRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryRemoveEnsureDeviceAwake"></a><a id="wdfdevstatepnpqueryremoveensuredeviceawake"></a><a id="WDFDEVSTATEPNPQUERYREMOVEENSUREDEVICEAWAKE"></a><b>WdfDevStatePnpQueryRemoveEnsureDeviceAwake</b>

<dd></dd>

### -field <a id="WdfDevStatePnpQueryStopEnsureDeviceAwake"></a><a id="wdfdevstatepnpquerystopensuredeviceawake"></a><a id="WDFDEVSTATEPNPQUERYSTOPENSUREDEVICEAWAKE"></a><b>WdfDevStatePnpQueryStopEnsureDeviceAwake</b>

<dd></dd>

### -field <a id="WdfDevStatePnpFailedPowerPolicyRemoved"></a><a id="wdfdevstatepnpfailedpowerpolicyremoved"></a><a id="WDFDEVSTATEPNPFAILEDPOWERPOLICYREMOVED"></a><b>WdfDevStatePnpFailedPowerPolicyRemoved</b>

<dd></dd>

### -field <a id="WdfDevStatePnpNull"></a><a id="wdfdevstatepnpnull"></a><a id="WDFDEVSTATEPNPNULL"></a><b>WdfDevStatePnpNull</b>

<dd></dd>
</dl>

## -remarks
<p>The WDF_DEVICE_PNP_STATE enumeration is used as a member type for  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551260">WDF_DEVICE_PNP_NOTIFICATION_DATA</a> structure and as the return type for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545969">WdfDeviceGetDevicePnpState</a> method.</p>

<p>The WDF_DEVICE_PNP_STATE enumeration is used as a member type for  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551260">WDF_DEVICE_PNP_NOTIFICATION_DATA</a> structure and as the return type for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545969">WdfDeviceGetDevicePnpState</a> method.</p>

<p>The WDF_DEVICE_PNP_STATE enumeration is used as a member type for  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551260">WDF_DEVICE_PNP_NOTIFICATION_DATA</a> structure and as the return type for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545969">WdfDeviceGetDevicePnpState</a> method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>