---
UID: NE.wdfdevice._WDF_DEVICE_PNP_STATE
title: WDF_DEVICE_PNP_STATE
author: windows-driver-content
description: The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter.
old-location: wdf\wdf_device_pnp_state.htm
old-project: wdf
ms.assetid: b907a1ca-d9ef-45e9-9e1b-26e58e3e1e07
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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

### -field WdfDevStatePnpInvalid

<dd></dd>

### -field WdfDevStatePnpObjectCreated

<dd></dd>

### -field WdfDevStatePnpCheckForDevicePresence

<dd></dd>

### -field WdfDevStatePnpEjectFailed

<dd></dd>

### -field WdfDevStatePnpEjectHardware

<dd></dd>

### -field WdfDevStatePnpEjectedWaitingForRemove

<dd></dd>

### -field WdfDevStatePnpInit

<dd></dd>

### -field WdfDevStatePnpInitStarting

<dd></dd>

### -field WdfDevStatePnpInitSurpriseRemoved

<dd></dd>

### -field WdfDevStatePnpHardwareAvailable

<dd></dd>

### -field WdfDevStatePnpEnableInterfaces

<dd></dd>

### -field WdfDevStatePnpHardwareAvailablePowerPolicyFailed

<dd></dd>

### -field WdfDevStatePnpQueryRemoveAskDriver

<dd></dd>

### -field WdfDevStatePnpQueryRemovePending

<dd></dd>

### -field WdfDevStatePnpQueryRemoveStaticCheck

<dd></dd>

### -field WdfDevStatePnpQueriedRemoving

<dd></dd>

### -field WdfDevStatePnpQueryStopAskDriver

<dd></dd>

### -field WdfDevStatePnpQueryStopPending

<dd></dd>

### -field WdfDevStatePnpQueryStopStaticCheck

<dd></dd>

### -field WdfDevStatePnpQueryCanceled

<dd></dd>

### -field WdfDevStatePnpRemoved

<dd></dd>

### -field WdfDevStatePnpPdoRemoved

<dd></dd>

### -field WdfDevStatePnpRemovedPdoWait

<dd></dd>

### -field WdfDevStatePnpRemovedPdoSurpriseRemoved

<dd></dd>

### -field WdfDevStatePnpRemovingDisableInterfaces

<dd></dd>

### -field WdfDevStatePnpRestarting

<dd></dd>

### -field WdfDevStatePnpStarted

<dd></dd>

### -field WdfDevStatePnpStartedCancelStop

<dd></dd>

### -field WdfDevStatePnpStartedCancelRemove

<dd></dd>

### -field WdfDevStatePnpStartedRemoving

<dd></dd>

### -field WdfDevStatePnpStartingFromStopped

<dd></dd>

### -field WdfDevStatePnpStopped

<dd></dd>

### -field WdfDevStatePnpStoppedWaitForStartCompletion

<dd></dd>

### -field WdfDevStatePnpStartedStopping

<dd></dd>

### -field WdfDevStatePnpSurpriseRemove

<dd></dd>

### -field WdfDevStatePnpInitQueryRemove

<dd></dd>

### -field WdfDevStatePnpInitQueryRemoveCanceled

<dd></dd>

### -field WdfDevStatePnpFdoRemoved

<dd></dd>

### -field WdfDevStatePnpRemovedWaitForChildren

<dd></dd>

### -field WdfDevStatePnpQueriedSurpriseRemove

<dd></dd>

### -field WdfDevStatePnpSurpriseRemoveIoStarted

<dd></dd>

### -field WdfDevStatePnpFailedPowerDown

<dd></dd>

### -field WdfDevStatePnpFailedIoStarting

<dd></dd>

### -field WdfDevStatePnpFailedOwnHardware

<dd></dd>

### -field WdfDevStatePnpFailed

<dd></dd>

### -field WdfDevStatePnpFailedSurpriseRemoved

<dd></dd>

### -field WdfDevStatePnpFailedStarted

<dd></dd>

### -field WdfDevStatePnpFailedWaitForRemove

<dd></dd>

### -field WdfDevStatePnpFailedInit

<dd></dd>

### -field WdfDevStatePnpPdoInitFailed

<dd></dd>

### -field WdfDevStatePnpRestart

<dd></dd>

### -field WdfDevStatePnpRestartReleaseHardware

<dd></dd>

### -field WdfDevStatePnpRestartHardwareAvailable

<dd></dd>

### -field WdfDevStatePnpPdoRestart

<dd></dd>

### -field WdfDevStatePnpFinal

<dd></dd>

### -field WdfDevStatePnpRemovedChildrenRemoved

<dd></dd>

### -field WdfDevStatePnpQueryRemoveEnsureDeviceAwake

<dd></dd>

### -field WdfDevStatePnpQueryStopEnsureDeviceAwake

<dd></dd>

### -field WdfDevStatePnpFailedPowerPolicyRemoved

<dd></dd>

### -field WdfDevStatePnpNull

<dd></dd>
</dl>

## -remarks
<p>The WDF_DEVICE_PNP_STATE enumeration is used as a member type for  the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-pnp-notification-data.md">WDF_DEVICE_PNP_NOTIFICATION_DATA</a> structure and as the return type for the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepnpstate.md">WdfDeviceGetDevicePnpState</a> method.</p>

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