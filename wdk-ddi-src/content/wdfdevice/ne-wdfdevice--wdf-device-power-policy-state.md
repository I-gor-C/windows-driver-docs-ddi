---
UID: NE.wdfdevice._WDF_DEVICE_POWER_POLICY_STATE
title: WDF_DEVICE_POWER_POLICY_STATE
author: windows-driver-content
description: The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter.
old-location: wdf\wdf_device_power_policy_state.htm
old-project: wdf
ms.assetid: 87fa78f7-417a-4720-9520-0eb90486630a
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
req.alt-api: WDF_DEVICE_POWER_POLICY_STATE
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

# WDF_DEVICE_POWER_POLICY_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter.</p>


## -syntax

````
typedef enum _WDF_DEVICE_POWER_POLICY_STATE { 
  WdfDevStatePwrPolInvalid                                                     = 0x00,
  WdfDevStatePwrPolObjectCreated                                               = 0x500,
  WdfDevStatePwrPolStarting                                                    = 0x501,
  WdfDevStatePwrPolStartingSucceeded                                           = 0x502,
  WdfDevStatePwrPolStartingFailed                                              = 0x503,
  WdfDevStatePwrPolStartingDecideS0Wake                                        = 0x504,
  WdfDevStatePwrPolStartedIdleCapable                                          = 0x505,
  WdfDevStatePwrPolTimerExpiredNoWake                                          = 0x506,
  WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown                         = 0x507,
  WdfDevStatePwrPolWaitingUnarmed                                              = 0x508,
  WdfDevStatePwrPolWaitingUnarmedQueryIdle                                     = 0x509,
  WdfDevStatePwrPolS0NoWakePowerUp                                             = 0x50A,
  WdfDevStatePwrPolS0NoWakeCompletePowerUp                                     = 0x50B,
  WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed                         = 0x50C,
  WdfDevStatePwrPolSystemSleepNeedWake                                         = 0x50D,
  WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp                          = 0x50E,
  WdfDevStatePwrPolSystemSleepPowerRequestFailed                               = 0x50F,
  WdfDevStatePwrPolCheckPowerPageable                                          = 0x510,
  WdfDevStatePwrPolSleepingWakeWakeArrived                                     = 0x511,
  WdfDevStatePwrPolSleepingWakeRevertArmWake                                   = 0x512,
  WdfDevStatePwrPolSystemAsleepWakeArmed                                       = 0x513,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabled                                 = 0x514,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled                     = 0x515,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisarm                                  = 0x516,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggered                               = 0x517,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0                             = 0x518,
  WdfDevStatePwrPolSystemWakeDeviceWokeDisarm                                  = 0x519,
  WdfDevStatePwrPolSleepingWakeWakeArrivedNP                                   = 0x51A | WdfDevStateNP,
  WdfDevStatePwrPolSleepingWakeRevertArmWakeNP                                 = 0x51B | WdfDevStateNP,
  WdfDevStatePwrPolSleepingWakePowerDownFailed                                 = 0x51C,
  WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled                     = 0x51D,
  WdfDevStatePwrPolSystemAsleepWakeArmedNP                                     = 0x51E | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP                               = 0x51F | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP                   = 0x520 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP                                = 0x521 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP                             = 0x522 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP                           = 0x523 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP                                = 0x524 | WdfDevStateNP,
  WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp                         = 0x525,
  WdfDevStatePwrPolSleeping                                                    = 0x526,
  WdfDevStatePwrPolSleepingNoWakePowerDown                                     = 0x527,
  WdfDevStatePwrPolSleepingNoWakeCompletePowerDown                             = 0x528,
  WdfDevStatePwrPolSleepingNoWakeDxRequestFailed                               = 0x529,
  WdfDevStatePwrPolSleepingWakePowerDown                                       = 0x52A,
  WdfDevStatePwrPolSleepingSendWake                                            = 0x52B,
  WdfDevStatePwrPolSystemAsleepNoWake                                          = 0x52C,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisabled                                = 0x52D,
  WdfDevStatePwrPolSystemWakeDeviceToD0                                        = 0x52E,
  WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp                         = 0x52F,
  WdfDevStatePwrPolSystemWakeQueryIdle                                         = 0x530,
  WdfDevStatePwrPolStartedWakeCapable                                          = 0x531,
  WdfDevStatePwrPolTimerExpiredDecideUsbSS                                     = 0x532,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown                            = 0x533,
  WdfDevStatePwrPolTimerExpiredWakeCapableSendWake                             = 0x534,
  WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS                                = 0x535,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived                          = 0x536,
  WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake                           = 0x537,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled                         = 0x538,
  WdfDevStatePwrPolTimerExpiredWakeCapableCleanup                              = 0x539,
  WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed                        = 0x53A,
  WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown                          = 0x53B,
  WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp                            = 0x53C,
  WdfDevStatePwrPolWaitingArmedUsbSS                                           = 0x53D,
  WdfDevStatePwrPolWaitingArmed                                                = 0x53E,
  WdfDevStatePwrPolWaitingArmedQueryIdle                                       = 0x53F,
  WdfDevStatePwrPolIoPresentArmed                                              = 0x540,
  WdfDevStatePwrPolIoPresentArmedWakeCanceled                                  = 0x541,
  WdfDevStatePwrPolS0WakeDisarm                                                = 0x542,
  WdfDevStatePwrPolS0WakeCompletePowerUp                                       = 0x543,
  WdfDevStatePwrPolTimerExpiredWakeSucceeded                                   = 0x544,
  WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm                             = 0x545,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded                        = 0x546,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed                           = 0x547,
  WdfDevStatePwrPolWakeFailedUsbSS                                             = 0x548,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake            = 0x549,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled          = 0x54A,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS                 = 0x54B,
  WdfDevStatePwrPolCancelingWakeForSystemSleep                                 = 0x54C,
  WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled                     = 0x54D,
  WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp                  = 0x54E,
  WdfDevStatePwrPolPowerUpForSystemSleepFailed                                 = 0x54F,
  WdfDevStatePwrPolWokeFromS0UsbSS                                             = 0x550,
  WdfDevStatePwrPolWokeFromS0                                                  = 0x551,
  WdfDevStatePwrPolWokeFromS0NotifyDriver                                      = 0x552,
  WdfDevStatePwrPolStoppingResetDevice                                         = 0x553,
  WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp                          = 0x554,
  WdfDevStatePwrPolStoppingResetDeviceFailed                                   = 0x555,
  WdfDevStatePwrPolStoppingD0                                                  = 0x556,
  WdfDevStatePwrPolStoppingD0Failed                                            = 0x557,
  WdfDevStatePwrPolStoppingDisarmWake                                          = 0x558,
  WdfDevStatePwrPolStoppingDisarmWakeCancelWake                                = 0x559,
  WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled                              = 0x55A,
  WdfDevStatePwrPolStopping                                                    = 0x55B,
  WdfDevStatePwrPolStoppingFailed                                              = 0x55C,
  WdfDevStatePwrPolStoppingSendStatus                                          = 0x55D,
  WdfDevStatePwrPolStoppingCancelTimer                                         = 0x55E,
  WdfDevStatePwrPolStoppingWaitForIdleTimeout                                  = 0x55F,
  WdfDevStatePwrPolStoppingCancelUsbSS                                         = 0x560,
  WdfDevStatePwrPolStoppingWaitForUsbSSCompletion                              = 0x561,
  WdfDevStatePwrPolStoppingCancelWake                                          = 0x562,
  WdfDevStatePwrPolStopped                                                     = 0x563,
  WdfDevStatePwrPolCancelUsbSS                                                 = 0x564,
  WdfDevStatePwrPolStarted                                                     = 0x565,
  WdfDevStatePwrPolStartedCancelTimer                                          = 0x566,
  WdfDevStatePwrPolStartedWaitForIdleTimeout                                   = 0x567,
  WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep                       = 0x568,
  WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout                        = 0x569,
  WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS                             = 0x56A,
  WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep                       = 0x56B,
  WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout                        = 0x56C,
  WdfDevStatePwrPolDeviceD0PowerRequestFailed                                  = 0x56D,
  WdfDevStatePwrPolDevicePowerRequestFailed                                    = 0x56E,
  WdfDevStatePwrPolGotoDx                                                      = 0x56F,
  WdfDevStatePwrPolGotoDxInDx                                                  = 0x570,
  WdfDevStatePwrPolDx                                                          = 0x571,
  WdfDevStatePwrPolGotoD0                                                      = 0x572,
  WdfDevStatePwrPolGotoD0InD0                                                  = 0x573,
  WdfDevStatePwrPolFinal                                                       = 0x574,
  WdfDevStatePwrPolSleepingPowerDownNotProcessed                               = 0x575,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed                = 0x576,
  WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed                     = 0x577,
  WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer               = 0x578,
  WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown                         = 0x579,
  WdfDevStatePwrPolStoppingPoweringUp                                          = 0x57A,
  WdfDevStatePwrPolStoppingPoweringDown                                        = 0x57B,
  WdfDevStatePwrPolPowerUpForSystemSleepNotSeen                                = 0x57C,
  WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS                             = 0x57D,
  WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS                           = 0x57E,
  WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS                            = 0x57F,
  WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS                        = 0x580,
  WdfDevStatePwrPolCancelingUsbSSForSystemSleep                                = 0x581,
  WdfDevStatePwrPolStoppingD0CancelUsbSS                                       = 0x582,
  WdfDevStatePwrPolStartingPoweredUp                                           = 0x583,
  WdfDevStatePwrPolIdleCapableDeviceIdle                                       = 0x584,
  WdfDevStatePwrPolDeviceIdleReturnToActive                                    = 0x585,
  WdfDevStatePwrPolDeviceIdleSleeping                                          = 0x586,
  WdfDevStatePwrPolDeviceIdleStopping                                          = 0x587,
  WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown                             = 0x588,
  WdfDevStatePwrPolWakeCapableDeviceIdle                                       = 0x589,
  WdfDevStatePwrPolWakeCapableUsbSSCompleted                                   = 0x58A,
  WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown                        = 0x58B,
  WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted                    = 0x58C,
  WdfDevStatePwrPolStoppedRemoving                                             = 0x58D,
  WdfDevStatePwrPolRemoved                                                     = 0x58E,
  WdfDevStatePwrPolRestarting                                                  = 0x58F,
  WdfDevStatePwrPolRestartingFailed                                            = 0x590,
  WdfDevStatePwrPolStartingPoweredUpFailed                                     = 0x591,
  WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive                            = 0x592,
  WdfDevStatePwrPolWaitingArmedWakeInterruptFired                              = 0x593,
  WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired                          = 0x594,
  WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP                        = 0x595 | WdfDevStateNP,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived                 = 0x596,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived  = 0x597,
  WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown               = 0x598,
  WdfDevStatePwrPolNull                                                        = 0x599
} WDF_DEVICE_POWER_POLICY_STATE, *PWDF_DEVICE_POWER_POLICY_STATE;
````


## -enum-fields
<dl>

### -field WdfDevStatePwrPolInvalid

<dd></dd>

### -field WdfDevStatePwrPolObjectCreated

<dd></dd>

### -field WdfDevStatePwrPolStarting

<dd></dd>

### -field WdfDevStatePwrPolStartingSucceeded

<dd></dd>

### -field WdfDevStatePwrPolStartingFailed

<dd></dd>

### -field WdfDevStatePwrPolStartingDecideS0Wake

<dd></dd>

### -field WdfDevStatePwrPolStartedIdleCapable

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredNoWake

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown

<dd></dd>

### -field WdfDevStatePwrPolWaitingUnarmed

<dd></dd>

### -field WdfDevStatePwrPolWaitingUnarmedQueryIdle

<dd></dd>

### -field WdfDevStatePwrPolS0NoWakePowerUp

<dd></dd>

### -field WdfDevStatePwrPolS0NoWakeCompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed

<dd></dd>

### -field WdfDevStatePwrPolSystemSleepNeedWake

<dd></dd>

### -field WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolSystemSleepPowerRequestFailed

<dd></dd>

### -field WdfDevStatePwrPolCheckPowerPageable

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakeWakeArrived

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakeRevertArmWake

<dd></dd>

### -field WdfDevStatePwrPolSystemAsleepWakeArmed

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeEnabled

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeDisarm

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeTriggered

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWokeDisarm

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakeWakeArrivedNP

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakeRevertArmWakeNP

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakePowerDownFailed

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolSystemAsleepWakeArmedNP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolSleeping

<dd></dd>

### -field WdfDevStatePwrPolSleepingNoWakePowerDown

<dd></dd>

### -field WdfDevStatePwrPolSleepingNoWakeCompletePowerDown

<dd></dd>

### -field WdfDevStatePwrPolSleepingNoWakeDxRequestFailed

<dd></dd>

### -field WdfDevStatePwrPolSleepingWakePowerDown

<dd></dd>

### -field WdfDevStatePwrPolSleepingSendWake

<dd></dd>

### -field WdfDevStatePwrPolSystemAsleepNoWake

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeDisabled

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceToD0

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeQueryIdle

<dd></dd>

### -field WdfDevStatePwrPolStartedWakeCapable

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredDecideUsbSS

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableSendWake

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableCleanup

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedUsbSS

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmed

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedQueryIdle

<dd></dd>

### -field WdfDevStatePwrPolIoPresentArmed

<dd></dd>

### -field WdfDevStatePwrPolIoPresentArmedWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolS0WakeDisarm

<dd></dd>

### -field WdfDevStatePwrPolS0WakeCompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeSucceeded

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed

<dd></dd>

### -field WdfDevStatePwrPolWakeFailedUsbSS

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS

<dd></dd>

### -field WdfDevStatePwrPolCancelingWakeForSystemSleep

<dd></dd>

### -field WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolPowerUpForSystemSleepFailed

<dd></dd>

### -field WdfDevStatePwrPolWokeFromS0UsbSS

<dd></dd>

### -field WdfDevStatePwrPolWokeFromS0

<dd></dd>

### -field WdfDevStatePwrPolWokeFromS0NotifyDriver

<dd></dd>

### -field WdfDevStatePwrPolStoppingResetDevice

<dd></dd>

### -field WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp

<dd></dd>

### -field WdfDevStatePwrPolStoppingResetDeviceFailed

<dd></dd>

### -field WdfDevStatePwrPolStoppingD0

<dd></dd>

### -field WdfDevStatePwrPolStoppingD0Failed

<dd></dd>

### -field WdfDevStatePwrPolStoppingDisarmWake

<dd></dd>

### -field WdfDevStatePwrPolStoppingDisarmWakeCancelWake

<dd></dd>

### -field WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled

<dd></dd>

### -field WdfDevStatePwrPolStopping

<dd></dd>

### -field WdfDevStatePwrPolStoppingFailed

<dd></dd>

### -field WdfDevStatePwrPolStoppingSendStatus

<dd></dd>

### -field WdfDevStatePwrPolStoppingCancelTimer

<dd></dd>

### -field WdfDevStatePwrPolStoppingWaitForIdleTimeout

<dd></dd>

### -field WdfDevStatePwrPolStoppingCancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolStoppingWaitForUsbSSCompletion

<dd></dd>

### -field WdfDevStatePwrPolStoppingCancelWake

<dd></dd>

### -field WdfDevStatePwrPolStopped

<dd></dd>

### -field WdfDevStatePwrPolCancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolStarted

<dd></dd>

### -field WdfDevStatePwrPolStartedCancelTimer

<dd></dd>

### -field WdfDevStatePwrPolStartedWaitForIdleTimeout

<dd></dd>

### -field WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep

<dd></dd>

### -field WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout

<dd></dd>

### -field WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS

<dd></dd>

### -field WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep

<dd></dd>

### -field WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout

<dd></dd>

### -field WdfDevStatePwrPolDeviceD0PowerRequestFailed

<dd></dd>

### -field WdfDevStatePwrPolDevicePowerRequestFailed

<dd></dd>

### -field WdfDevStatePwrPolGotoDx

<dd></dd>

### -field WdfDevStatePwrPolGotoDxInDx

<dd></dd>

### -field WdfDevStatePwrPolDx

<dd></dd>

### -field WdfDevStatePwrPolGotoD0

<dd></dd>

### -field WdfDevStatePwrPolGotoD0InD0

<dd></dd>

### -field WdfDevStatePwrPolFinal

<dd></dd>

### -field WdfDevStatePwrPolSleepingPowerDownNotProcessed

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer

<dd></dd>

### -field WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown

<dd></dd>

### -field WdfDevStatePwrPolStoppingPoweringUp

<dd></dd>

### -field WdfDevStatePwrPolStoppingPoweringDown

<dd></dd>

### -field WdfDevStatePwrPolPowerUpForSystemSleepNotSeen

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolCancelingUsbSSForSystemSleep

<dd></dd>

### -field WdfDevStatePwrPolStoppingD0CancelUsbSS

<dd></dd>

### -field WdfDevStatePwrPolStartingPoweredUp

<dd></dd>

### -field WdfDevStatePwrPolIdleCapableDeviceIdle

<dd></dd>

### -field WdfDevStatePwrPolDeviceIdleReturnToActive

<dd></dd>

### -field WdfDevStatePwrPolDeviceIdleSleeping

<dd></dd>

### -field WdfDevStatePwrPolDeviceIdleStopping

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown

<dd></dd>

### -field WdfDevStatePwrPolWakeCapableDeviceIdle

<dd></dd>

### -field WdfDevStatePwrPolWakeCapableUsbSSCompleted

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted

<dd></dd>

### -field WdfDevStatePwrPolStoppedRemoving

<dd></dd>

### -field WdfDevStatePwrPolRemoved

<dd></dd>

### -field WdfDevStatePwrPolRestarting

<dd></dd>

### -field WdfDevStatePwrPolRestartingFailed

<dd></dd>

### -field WdfDevStatePwrPolStartingPoweredUpFailed

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedWakeInterruptFired

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired

<dd></dd>

### -field WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived

<dd></dd>

### -field WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived

<dd></dd>

### -field WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown

<dd></dd>

### -field WdfDevStatePwrPolNull

<dd></dd>
</dl>

## -remarks
<p>The WDF_DEVICE_POWER_POLICY_STATE enumeration is used as a member type in the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-notification-data.md">WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA</a> structure and as the return type for the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerpolicystate.md">WdfDeviceGetDevicePowerPolicyState</a> method.</p>

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