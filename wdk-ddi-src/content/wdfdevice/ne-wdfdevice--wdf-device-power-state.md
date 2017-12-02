---
UID: NE.wdfdevice._WDF_DEVICE_POWER_STATE
title: WDF_DEVICE_POWER_STATE
author: windows-driver-content
description: The WDF_DEVICE_POWER_STATE enumeration identifies all of the states that the framework's power state machine can enter.
old-location: wdf\wdf_device_power_state.htm
old-project: wdf
ms.assetid: 06bb6465-afc6-4b92-b3d7-1c66f6c6c33d
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
req.alt-api: WDF_DEVICE_POWER_STATE
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

# WDF_DEVICE_POWER_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DEVICE_POWER_STATE</b> enumeration identifies all of the states that the framework's power state machine can enter.</p>


## -syntax

````
typedef enum _WDF_DEVICE_POWER_STATE { 
  WdfDevStatePowerInvalid                             = 0x00,
  WdfDevStatePowerObjectCreated                       = 0x300,
  WdfDevStatePowerCheckDeviceType                     = 0x301,
  WdfDevStatePowerCheckDeviceTypeNP                   = 0x302 | WdfDevStateNP,
  WdfDevStatePowerCheckParentState                    = 0x303,
  WdfDevStatePowerCheckParentStateNP                  = 0x304 | WdfDevStateNP,
  WdfDevStatePowerEnablingWakeAtBus                   = 0x305,
  WdfDevStatePowerEnablingWakeAtBusNP                 = 0x306 | WdfDevStateNP,
  WdfDevStatePowerD0                                  = 0x307,
  WdfDevStatePowerD0NP                                = 0x308 | WdfDevStateNP,
  WdfDevStatePowerD0BusWakeOwner                      = 0x309,
  WdfDevStatePowerD0BusWakeOwnerNP                    = 0x30A | WdfDevStateNP,
  WdfDevStatePowerD0ArmedForWake                      = 0x30B,
  WdfDevStatePowerD0ArmedForWakeNP                    = 0x30C | WdfDevStateNP,
  WdfDevStatePowerD0DisarmingWakeAtBus                = 0x30D,
  WdfDevStatePowerD0DisarmingWakeAtBusNP              = 0x30E | WdfDevStateNP,
  WdfDevStatePowerD0Starting                          = 0x30F,
  WdfDevStatePowerD0StartingConnectInterrupt          = 0x310,
  WdfDevStatePowerD0StartingDmaEnable                 = 0x311,
  WdfDevStatePowerD0StartingStartSelfManagedIo        = 0x312,
  WdfDevStatePowerDecideD0State                       = 0x313,
  WdfDevStatePowerGotoD3Stopped                       = 0x314,
  WdfDevStatePowerStopped                             = 0x315,
  WdfDevStatePowerStartingCheckDeviceType             = 0x316,
  WdfDevStatePowerStartingChild                       = 0x317,
  WdfDevStatePowerDxDisablingWakeAtBus                = 0x318,
  WdfDevStatePowerDxDisablingWakeAtBusNP              = 0x319 | WdfDevStateNP,
  WdfDevStatePowerGotoDx                              = 0x31A,
  WdfDevStatePowerGotoDxNP                            = 0x31B | WdfDevStateNP,
  WdfDevStatePowerGotoDxIoStopped                     = 0x31C,
  WdfDevStatePowerGotoDxIoStoppedNP                   = 0x31D | WdfDevStateNP,
  WdfDevStatePowerGotoDxNPFailed                      = 0x31E | WdfDevStateNP,
  WdfDevStatePowerDx                                  = 0x31F,
  WdfDevStatePowerDxNP                                = 0x320 | WdfDevStateNP,
  WdfDevStatePowerGotoDxArmedForWake                  = 0x321,
  WdfDevStatePowerGotoDxArmedForWakeNP                = 0x322 | WdfDevStateNP,
  WdfDevStatePowerGotoDxIoStoppedArmedForWake         = 0x323,
  WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP       = 0x324 | WdfDevStateNP,
  WdfDevStatePowerDxArmedForWake                      = 0x325,
  WdfDevStatePowerDxArmedForWakeNP                    = 0x326 | WdfDevStateNP,
  WdfDevStatePowerCheckParentStateArmedForWake        = 0x327,
  WdfDevStatePowerCheckParentStateArmedForWakeNP      = 0x328 | WdfDevStateNP,
  WdfDevStatePowerWaitForParentArmedForWake           = 0x329,
  WdfDevStatePowerWaitForParentArmedForWakeNP         = 0x32A | WdfDevStateNP,
  WdfDevStatePowerStartSelfManagedIo                  = 0x32B,
  WdfDevStatePowerStartSelfManagedIoNP                = 0x32C | WdfDevStateNP,
  WdfDevStatePowerStartSelfManagedIoFailed            = 0x32D,
  WdfDevStatePowerStartSelfManagedIoFailedNP          = 0x32E | WdfDevStateNP,
  WdfDevStatePowerWaitForParent                       = 0x32F,
  WdfDevStatePowerWaitForParentNP                     = 0x330 | WdfDevStateNP,
  WdfDevStatePowerWakePending                         = 0x331,
  WdfDevStatePowerWakePendingNP                       = 0x332 | WdfDevStateNP,
  WdfDevStatePowerWaking                              = 0x333,
  WdfDevStatePowerWakingNP                            = 0x334 | WdfDevStateNP,
  WdfDevStatePowerWakingConnectInterrupt              = 0x335,
  WdfDevStatePowerWakingConnectInterruptNP            = 0x336 | WdfDevStateNP,
  WdfDevStatePowerWakingConnectInterruptFailed        = 0x337,
  WdfDevStatePowerWakingConnectInterruptFailedNP      = 0x338 | WdfDevStateNP,
  WdfDevStatePowerWakingDmaEnable                     = 0x339,
  WdfDevStatePowerWakingDmaEnableNP                   = 0x33A | WdfDevStateNP,
  WdfDevStatePowerWakingDmaEnableFailed               = 0x33B,
  WdfDevStatePowerWakingDmaEnableFailedNP             = 0x33C | WdfDevStateNP,
  WdfDevStatePowerReportPowerUpFailedDerefParent      = 0x33D,
  WdfDevStatePowerReportPowerUpFailed                 = 0x33E,
  WdfDevStatePowerPowerFailedPowerDown                = 0x33F,
  WdfDevStatePowerReportPowerDownFailed               = 0x340,
  WdfDevStatePowerInitialConnectInterruptFailed       = 0x341,
  WdfDevStatePowerInitialDmaEnableFailed              = 0x342,
  WdfDevStatePowerInitialSelfManagedIoFailed          = 0x343,
  WdfDevStatePowerInitialPowerUpFailedDerefParent     = 0x344,
  WdfDevStatePowerInitialPowerUpFailed                = 0x345,
  WdfDevStatePowerDxStoppedDisarmWake                 = 0x346,
  WdfDevStatePowerDxStoppedDisarmWakeNP               = 0x347 | WdfDevStateNP,
  WdfDevStatePowerGotoDxStoppedDisableInterruptNP     = 0x348 | WdfDevStateNP,
  WdfDevStatePowerGotoDxStopped                       = 0x349,
  WdfDevStatePowerDxStopped                           = 0x34A,
  WdfDevStatePowerGotoStopped                         = 0x34B,
  WdfDevStatePowerStoppedCompleteDx                   = 0x34C,
  WdfDevStatePowerDxStoppedDecideDxState              = 0x34D,
  WdfDevStatePowerDxStoppedArmForWake                 = 0x34E,
  WdfDevStatePowerDxStoppedArmForWakeNP               = 0x34F | WdfDevStateNP,
  WdfDevStatePowerFinalPowerDownFailed                = 0x350,
  WdfDevStatePowerFinal                               = 0x351,
  WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus       = 0x352,
  WdfDevStatePowerUpFailed                            = 0x353,
  WdfDevStatePowerUpFailedDerefParent                 = 0x354,
  WdfDevStatePowerGotoDxFailed                        = 0x355,
  WdfDevStatePowerGotoDxStoppedDisableInterrupt       = 0x356,
  WdfDevStatePowerUpFailedNP                          = 0x357 | WdfDevStateNP,
  WdfDevStatePowerUpFailedDerefParentNP               = 0x358 | WdfDevStateNP,
  WdfDevStatePowerNotifyingD0ExitToWakeInterrupts     = 0x359,
  WdfDevStatePowerNotifyingD0EntryToWakeInterrupts    = 0x35A,
  WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP   = 0x35B | WdfDevStateNP,
  WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP  = 0x35C | WdfDevStateNP,
  WdfDevStatePowerInitialPowerUpFailedPowerDown       = 0x35D,
  WdfDevStatePowerUpFailedPowerDown                   = 0x35E,
  WdfDevStatePowerUpFailedPowerDownNP                 = 0x35F | WdfDevStateNP,
  WdfDevStatePowerInitialSelfManagedIoFailedStarted   = 0x360,
  WdfDevStatePowerStartSelfManagedIoFailedStarted     = 0x361,
  WdfDevStatePowerStartSelfManagedIoFailedStartedNP   = 0x362 | WdfDevStateNP,
  WdfDevStatePowerNull                                = 0x363
} WDF_DEVICE_POWER_STATE, *PWDF_DEVICE_POWER_STATE;
````


## -enum-fields
<dl>

### -field WdfDevStatePowerInvalid

<dd></dd>

### -field WdfDevStatePowerObjectCreated

<dd></dd>

### -field WdfDevStatePowerCheckDeviceType

<dd></dd>

### -field WdfDevStatePowerCheckDeviceTypeNP

<dd></dd>

### -field WdfDevStatePowerCheckParentState

<dd></dd>

### -field WdfDevStatePowerCheckParentStateNP

<dd></dd>

### -field WdfDevStatePowerEnablingWakeAtBus

<dd></dd>

### -field WdfDevStatePowerEnablingWakeAtBusNP

<dd></dd>

### -field WdfDevStatePowerD0

<dd></dd>

### -field WdfDevStatePowerD0NP

<dd></dd>

### -field WdfDevStatePowerD0BusWakeOwner

<dd></dd>

### -field WdfDevStatePowerD0BusWakeOwnerNP

<dd></dd>

### -field WdfDevStatePowerD0ArmedForWake

<dd></dd>

### -field WdfDevStatePowerD0ArmedForWakeNP

<dd></dd>

### -field WdfDevStatePowerD0DisarmingWakeAtBus

<dd></dd>

### -field WdfDevStatePowerD0DisarmingWakeAtBusNP

<dd></dd>

### -field WdfDevStatePowerD0Starting

<dd></dd>

### -field WdfDevStatePowerD0StartingConnectInterrupt

<dd></dd>

### -field WdfDevStatePowerD0StartingDmaEnable

<dd></dd>

### -field WdfDevStatePowerD0StartingStartSelfManagedIo

<dd></dd>

### -field WdfDevStatePowerDecideD0State

<dd></dd>

### -field WdfDevStatePowerGotoD3Stopped

<dd></dd>

### -field WdfDevStatePowerStopped

<dd></dd>

### -field WdfDevStatePowerStartingCheckDeviceType

<dd></dd>

### -field WdfDevStatePowerStartingChild

<dd></dd>

### -field WdfDevStatePowerDxDisablingWakeAtBus

<dd></dd>

### -field WdfDevStatePowerDxDisablingWakeAtBusNP

<dd></dd>

### -field WdfDevStatePowerGotoDx

<dd></dd>

### -field WdfDevStatePowerGotoDxNP

<dd></dd>

### -field WdfDevStatePowerGotoDxIoStopped

<dd></dd>

### -field WdfDevStatePowerGotoDxIoStoppedNP

<dd></dd>

### -field WdfDevStatePowerGotoDxNPFailed

<dd></dd>

### -field WdfDevStatePowerDx

<dd></dd>

### -field WdfDevStatePowerDxNP

<dd></dd>

### -field WdfDevStatePowerGotoDxArmedForWake

<dd></dd>

### -field WdfDevStatePowerGotoDxArmedForWakeNP

<dd></dd>

### -field WdfDevStatePowerGotoDxIoStoppedArmedForWake

<dd></dd>

### -field WdfDevStatePowerGotoDxIoStoppedArmedForWakeNP

<dd></dd>

### -field WdfDevStatePowerDxArmedForWake

<dd></dd>

### -field WdfDevStatePowerDxArmedForWakeNP

<dd></dd>

### -field WdfDevStatePowerCheckParentStateArmedForWake

<dd></dd>

### -field WdfDevStatePowerCheckParentStateArmedForWakeNP

<dd></dd>

### -field WdfDevStatePowerWaitForParentArmedForWake

<dd></dd>

### -field WdfDevStatePowerWaitForParentArmedForWakeNP

<dd></dd>

### -field WdfDevStatePowerStartSelfManagedIo

<dd></dd>

### -field WdfDevStatePowerStartSelfManagedIoNP

<dd></dd>

### -field WdfDevStatePowerStartSelfManagedIoFailed

<dd></dd>

### -field WdfDevStatePowerStartSelfManagedIoFailedNP

<dd></dd>

### -field WdfDevStatePowerWaitForParent

<dd></dd>

### -field WdfDevStatePowerWaitForParentNP

<dd></dd>

### -field WdfDevStatePowerWakePending

<dd></dd>

### -field WdfDevStatePowerWakePendingNP

<dd></dd>

### -field WdfDevStatePowerWaking

<dd></dd>

### -field WdfDevStatePowerWakingNP

<dd></dd>

### -field WdfDevStatePowerWakingConnectInterrupt

<dd></dd>

### -field WdfDevStatePowerWakingConnectInterruptNP

<dd></dd>

### -field WdfDevStatePowerWakingConnectInterruptFailed

<dd></dd>

### -field WdfDevStatePowerWakingConnectInterruptFailedNP

<dd></dd>

### -field WdfDevStatePowerWakingDmaEnable

<dd></dd>

### -field WdfDevStatePowerWakingDmaEnableNP

<dd></dd>

### -field WdfDevStatePowerWakingDmaEnableFailed

<dd></dd>

### -field WdfDevStatePowerWakingDmaEnableFailedNP

<dd></dd>

### -field WdfDevStatePowerReportPowerUpFailedDerefParent

<dd></dd>

### -field WdfDevStatePowerReportPowerUpFailed

<dd></dd>

### -field WdfDevStatePowerPowerFailedPowerDown

<dd></dd>

### -field WdfDevStatePowerReportPowerDownFailed

<dd></dd>

### -field WdfDevStatePowerInitialConnectInterruptFailed

<dd></dd>

### -field WdfDevStatePowerInitialDmaEnableFailed

<dd></dd>

### -field WdfDevStatePowerInitialSelfManagedIoFailed

<dd></dd>

### -field WdfDevStatePowerInitialPowerUpFailedDerefParent

<dd></dd>

### -field WdfDevStatePowerInitialPowerUpFailed

<dd></dd>

### -field WdfDevStatePowerDxStoppedDisarmWake

<dd></dd>

### -field WdfDevStatePowerDxStoppedDisarmWakeNP

<dd></dd>

### -field WdfDevStatePowerGotoDxStoppedDisableInterruptNP

<dd></dd>

### -field WdfDevStatePowerGotoDxStopped

<dd></dd>

### -field WdfDevStatePowerDxStopped

<dd></dd>

### -field WdfDevStatePowerGotoStopped

<dd></dd>

### -field WdfDevStatePowerStoppedCompleteDx

<dd></dd>

### -field WdfDevStatePowerDxStoppedDecideDxState

<dd></dd>

### -field WdfDevStatePowerDxStoppedArmForWake

<dd></dd>

### -field WdfDevStatePowerDxStoppedArmForWakeNP

<dd></dd>

### -field WdfDevStatePowerFinalPowerDownFailed

<dd></dd>

### -field WdfDevStatePowerFinal

<dd></dd>

### -field WdfDevStatePowerGotoImplicitD3DisarmWakeAtBus

<dd></dd>

### -field WdfDevStatePowerUpFailed

<dd></dd>

### -field WdfDevStatePowerUpFailedDerefParent

<dd></dd>

### -field WdfDevStatePowerGotoDxFailed

<dd></dd>

### -field WdfDevStatePowerGotoDxStoppedDisableInterrupt

<dd></dd>

### -field WdfDevStatePowerUpFailedNP

<dd></dd>

### -field WdfDevStatePowerUpFailedDerefParentNP

<dd></dd>

### -field WdfDevStatePowerNotifyingD0ExitToWakeInterrupts

<dd></dd>

### -field WdfDevStatePowerNotifyingD0EntryToWakeInterrupts

<dd></dd>

### -field WdfDevStatePowerNotifyingD0ExitToWakeInterruptsNP

<dd></dd>

### -field WdfDevStatePowerNotifyingD0EntryToWakeInterruptsNP

<dd></dd>

### -field WdfDevStatePowerInitialPowerUpFailedPowerDown

<dd></dd>

### -field WdfDevStatePowerUpFailedPowerDown

<dd></dd>

### -field WdfDevStatePowerUpFailedPowerDownNP

<dd></dd>

### -field WdfDevStatePowerInitialSelfManagedIoFailedStarted

<dd></dd>

### -field WdfDevStatePowerStartSelfManagedIoFailedStarted

<dd></dd>

### -field WdfDevStatePowerStartSelfManagedIoFailedStartedNP

<dd></dd>

### -field WdfDevStatePowerNull

<dd></dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_POWER_STATE</b> enumeration is used as a member type in the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-notification-data.md">WDF_DEVICE_POWER_NOTIFICATION_DATA</a> structure and as the return type for the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerstate.md">WdfDeviceGetDevicePowerState</a> method.</p>

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