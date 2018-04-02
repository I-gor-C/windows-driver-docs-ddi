---
UID: NE:wdfdevice._WDF_DEVICE_POWER_POLICY_STATE
title: "_WDF_DEVICE_POWER_POLICY_STATE"
author: windows-driver-content
description: The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter.
old-location: wdf\wdf_device_power_policy_state.htm
old-project: wdf
ms.assetid: 87fa78f7-417a-4720-9520-0eb90486630a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_DEVICE_POWER_POLICY_STATE, DFDeviceObjectGeneralRef_c80b69a2-86ba-4826-a48b-0ea80b47be01.xml, PWDF_DEVICE_POWER_POLICY_STATE, PWDF_DEVICE_POWER_POLICY_STATE enumeration pointer, WDF_DEVICE_POWER_POLICY_STATE, WDF_DEVICE_POWER_POLICY_STATE enumeration, WdfDevStatePwrPolCancelUsbSS, WdfDevStatePwrPolCancelingUsbSSForSystemSleep, WdfDevStatePwrPolCancelingWakeForSystemSleep, WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled, WdfDevStatePwrPolCheckPowerPageable, WdfDevStatePwrPolDeviceD0PowerRequestFailed, WdfDevStatePwrPolDeviceIdleReturnToActive, WdfDevStatePwrPolDeviceIdleSleeping, WdfDevStatePwrPolDeviceIdleStopping, WdfDevStatePwrPolDevicePowerRequestFailed, WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp, WdfDevStatePwrPolDx, WdfDevStatePwrPolFinal, WdfDevStatePwrPolGotoD0, WdfDevStatePwrPolGotoD0InD0, WdfDevStatePwrPolGotoDx, WdfDevStatePwrPolGotoDxInDx, WdfDevStatePwrPolIdleCapableDeviceIdle, WdfDevStatePwrPolInvalid, WdfDevStatePwrPolIoPresentArmed, WdfDevStatePwrPolIoPresentArmedWakeCanceled, WdfDevStatePwrPolNull, WdfDevStatePwrPolObjectCreated, WdfDevStatePwrPolPowerUpForSystemSleepFailed, WdfDevStatePwrPolPowerUpForSystemSleepNotSeen, WdfDevStatePwrPolRemoved, WdfDevStatePwrPolRestarting, WdfDevStatePwrPolRestartingFailed, WdfDevStatePwrPolS0NoWakeCompletePowerUp, WdfDevStatePwrPolS0NoWakePowerUp, WdfDevStatePwrPolS0WakeCompletePowerUp, WdfDevStatePwrPolS0WakeDisarm, WdfDevStatePwrPolSleeping, WdfDevStatePwrPolSleepingNoWakeCompletePowerDown, WdfDevStatePwrPolSleepingNoWakeDxRequestFailed, WdfDevStatePwrPolSleepingNoWakePowerDown, WdfDevStatePwrPolSleepingPowerDownNotProcessed, WdfDevStatePwrPolSleepingSendWake, WdfDevStatePwrPolSleepingWakePowerDown, WdfDevStatePwrPolSleepingWakePowerDownFailed, WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled, WdfDevStatePwrPolSleepingWakeRevertArmWake, WdfDevStatePwrPolSleepingWakeRevertArmWakeNP, WdfDevStatePwrPolSleepingWakeWakeArrived, WdfDevStatePwrPolSleepingWakeWakeArrivedNP, WdfDevStatePwrPolStarted, WdfDevStatePwrPolStartedCancelTimer, WdfDevStatePwrPolStartedIdleCapable, WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep, WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout, WdfDevStatePwrPolStartedWaitForIdleTimeout, WdfDevStatePwrPolStartedWakeCapable, WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep, WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS, WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout, WdfDevStatePwrPolStarting, WdfDevStatePwrPolStartingDecideS0Wake, WdfDevStatePwrPolStartingFailed, WdfDevStatePwrPolStartingPoweredUp, WdfDevStatePwrPolStartingPoweredUpFailed, WdfDevStatePwrPolStartingSucceeded, WdfDevStatePwrPolStopped, WdfDevStatePwrPolStoppedRemoving, WdfDevStatePwrPolStopping, WdfDevStatePwrPolStoppingCancelTimer, WdfDevStatePwrPolStoppingCancelUsbSS, WdfDevStatePwrPolStoppingCancelWake, WdfDevStatePwrPolStoppingD0, WdfDevStatePwrPolStoppingD0CancelUsbSS, WdfDevStatePwrPolStoppingD0Failed, WdfDevStatePwrPolStoppingDisarmWake, WdfDevStatePwrPolStoppingDisarmWakeCancelWake, WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled, WdfDevStatePwrPolStoppingFailed, WdfDevStatePwrPolStoppingPoweringDown, WdfDevStatePwrPolStoppingPoweringUp, WdfDevStatePwrPolStoppingResetDevice, WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp, WdfDevStatePwrPolStoppingResetDeviceFailed, WdfDevStatePwrPolStoppingSendStatus, WdfDevStatePwrPolStoppingWaitForIdleTimeout, WdfDevStatePwrPolStoppingWaitForUsbSSCompletion, WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown, WdfDevStatePwrPolSystemAsleepNoWake, WdfDevStatePwrPolSystemAsleepWakeArmed, WdfDevStatePwrPolSystemAsleepWakeArmedNP, WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed, WdfDevStatePwrPolSystemSleepNeedWake, WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp, WdfDevStatePwrPolSystemSleepPowerRequestFailed, WdfDevStatePwrPolSystemWakeDeviceToD0, WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp, WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp, WdfDevStatePwrPolSystemWakeDeviceWakeDisabled, WdfDevStatePwrPolSystemWakeDeviceWakeDisarm, WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP, WdfDevStatePwrPolSystemWakeDeviceWakeEnabled, WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP, WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled, WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP, WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired, WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP, WdfDevStatePwrPolSystemWakeDeviceWakeTriggered, WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP, WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0, WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP, WdfDevStatePwrPolSystemWakeDeviceWokeDisarm, WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP, WdfDevStatePwrPolSystemWakeQueryIdle, WdfDevStatePwrPolTimerExpiredDecideUsbSS, WdfDevStatePwrPolTimerExpiredNoWake, WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown, WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed, WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer, WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive, WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown, WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake, WdfDevStatePwrPolTimerExpiredWakeCapableCleanup, WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed, WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown, WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake, WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS, WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled, WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived, WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed, WdfDevStatePwrPolTimerExpiredWakeCapableSendWake, WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown, WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS, WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived, WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled, WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed, WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived, WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded, WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm, WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted, WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown, WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp, WdfDevStatePwrPolTimerExpiredWakeSucceeded, WdfDevStatePwrPolWaitingArmed, WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS, WdfDevStatePwrPolWaitingArmedQueryIdle, WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS, WdfDevStatePwrPolWaitingArmedUsbSS, WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS, WdfDevStatePwrPolWaitingArmedWakeInterruptFired, WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown, WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS, WdfDevStatePwrPolWaitingUnarmed, WdfDevStatePwrPolWaitingUnarmedQueryIdle, WdfDevStatePwrPolWakeCapableDeviceIdle, WdfDevStatePwrPolWakeCapableUsbSSCompleted, WdfDevStatePwrPolWakeFailedUsbSS, WdfDevStatePwrPolWokeFromS0, WdfDevStatePwrPolWokeFromS0NotifyDriver, WdfDevStatePwrPolWokeFromS0UsbSS, _WDF_DEVICE_POWER_POLICY_STATE, kmdf.wdf_device_power_policy_state, wdf.wdf_device_power_policy_state, wdfdevice/PWDF_DEVICE_POWER_POLICY_STATE, wdfdevice/WDF_DEVICE_POWER_POLICY_STATE, wdfdevice/WdfDevStatePwrPolCancelUsbSS, wdfdevice/WdfDevStatePwrPolCancelingUsbSSForSystemSleep, wdfdevice/WdfDevStatePwrPolCancelingWakeForSystemSleep, wdfdevice/WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled, wdfdevice/WdfDevStatePwrPolCheckPowerPageable, wdfdevice/WdfDevStatePwrPolDeviceD0PowerRequestFailed, wdfdevice/WdfDevStatePwrPolDeviceIdleReturnToActive, wdfdevice/WdfDevStatePwrPolDeviceIdleSleeping, wdfdevice/WdfDevStatePwrPolDeviceIdleStopping, wdfdevice/WdfDevStatePwrPolDevicePowerRequestFailed, wdfdevice/WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp, wdfdevice/WdfDevStatePwrPolDx, wdfdevice/WdfDevStatePwrPolFinal, wdfdevice/WdfDevStatePwrPolGotoD0, wdfdevice/WdfDevStatePwrPolGotoD0InD0, wdfdevice/WdfDevStatePwrPolGotoDx, wdfdevice/WdfDevStatePwrPolGotoDxInDx, wdfdevice/WdfDevStatePwrPolIdleCapableDeviceIdle, wdfdevice/WdfDevStatePwrPolInvalid, wdfdevice/WdfDevStatePwrPolIoPresentArmed, wdfdevice/WdfDevStatePwrPolIoPresentArmedWakeCanceled, wdfdevice/WdfDevStatePwrPolNull, wdfdevice/WdfDevStatePwrPolObjectCreated, wdfdevice/WdfDevStatePwrPolPowerUpForSystemSleepFailed, wdfdevice/WdfDevStatePwrPolPowerUpForSystemSleepNotSeen, wdfdevice/WdfDevStatePwrPolRemoved, wdfdevice/WdfDevStatePwrPolRestarting, wdfdevice/WdfDevStatePwrPolRestartingFailed, wdfdevice/WdfDevStatePwrPolS0NoWakeCompletePowerUp, wdfdevice/WdfDevStatePwrPolS0NoWakePowerUp, wdfdevice/WdfDevStatePwrPolS0WakeCompletePowerUp, wdfdevice/WdfDevStatePwrPolS0WakeDisarm, wdfdevice/WdfDevStatePwrPolSleeping, wdfdevice/WdfDevStatePwrPolSleepingNoWakeCompletePowerDown, wdfdevice/WdfDevStatePwrPolSleepingNoWakeDxRequestFailed, wdfdevice/WdfDevStatePwrPolSleepingNoWakePowerDown, wdfdevice/WdfDevStatePwrPolSleepingPowerDownNotProcessed, wdfdevice/WdfDevStatePwrPolSleepingSendWake, wdfdevice/WdfDevStatePwrPolSleepingWakePowerDown, wdfdevice/WdfDevStatePwrPolSleepingWakePowerDownFailed, wdfdevice/WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled, wdfdevice/WdfDevStatePwrPolSleepingWakeRevertArmWake, wdfdevice/WdfDevStatePwrPolSleepingWakeRevertArmWakeNP, wdfdevice/WdfDevStatePwrPolSleepingWakeWakeArrived, wdfdevice/WdfDevStatePwrPolSleepingWakeWakeArrivedNP, wdfdevice/WdfDevStatePwrPolStarted, wdfdevice/WdfDevStatePwrPolStartedCancelTimer, wdfdevice/WdfDevStatePwrPolStartedIdleCapable, wdfdevice/WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep, wdfdevice/WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout, wdfdevice/WdfDevStatePwrPolStartedWaitForIdleTimeout, wdfdevice/WdfDevStatePwrPolStartedWakeCapable, wdfdevice/WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep, wdfdevice/WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS, wdfdevice/WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout, wdfdevice/WdfDevStatePwrPolStarting, wdfdevice/WdfDevStatePwrPolStartingDecideS0Wake, wdfdevice/WdfDevStatePwrPolStartingFailed, wdfdevice/WdfDevStatePwrPolStartingPoweredUp, wdfdevice/WdfDevStatePwrPolStartingPoweredUpFailed, wdfdevice/WdfDevStatePwrPolStartingSucceeded, wdfdevice/WdfDevStatePwrPolStopped, wdfdevice/WdfDevStatePwrPolStoppedRemoving, wdfdevice/WdfDevStatePwrPolStopping, wdfdevice/WdfDevStatePwrPolStoppingCancelTimer, wdfdevice/WdfDevStatePwrPolStoppingCancelUsbSS, wdfdevice/WdfDevStatePwrPolStoppingCancelWake, wdfdevice/WdfDevStatePwrPolStoppingD0, wdfdevice/WdfDevStatePwrPolStoppingD0CancelUsbSS, wdfdevice/WdfDevStatePwrPolStoppingD0Failed, wdfdevice/WdfDevStatePwrPolStoppingDisarmWake, wdfdevice/WdfDevStatePwrPolStoppingDisarmWakeCancelWake, wdfdevice/WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled, wdfdevice/WdfDevStatePwrPolStoppingFailed, wdfdevice/WdfDevStatePwrPolStoppingPoweringDown, wdfdevice/WdfDevStatePwrPolStoppingPoweringUp, wdfdevice/WdfDevStatePwrPolStoppingResetDevice, wdfdevice/WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp, wdfdevice/WdfDevStatePwrPolStoppingResetDeviceFailed, wdfdevice/WdfDevStatePwrPolStoppingSendStatus, wdfdevice/WdfDevStatePwrPolStoppingWaitForIdleTimeout, wdfdevice/WdfDevStatePwrPolStoppingWaitForUsbSSCompletion, wdfdevice/WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown, wdfdevice/WdfDevStatePwrPolSystemAsleepNoWake, wdfdevice/WdfDevStatePwrPolSystemAsleepWakeArmed, wdfdevice/WdfDevStatePwrPolSystemAsleepWakeArmedNP, wdfdevice/WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed, wdfdevice/WdfDevStatePwrPolSystemSleepNeedWake, wdfdevice/WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp, wdfdevice/WdfDevStatePwrPolSystemSleepPowerRequestFailed, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceToD0, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeDisabled, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeDisarm, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeEnabled, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeTriggered, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWokeDisarm, wdfdevice/WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP, wdfdevice/WdfDevStatePwrPolSystemWakeQueryIdle, wdfdevice/WdfDevStatePwrPolTimerExpiredDecideUsbSS, wdfdevice/WdfDevStatePwrPolTimerExpiredNoWake, wdfdevice/WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown, wdfdevice/WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed, wdfdevice/WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer, wdfdevice/WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive, wdfdevice/WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableCleanup, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableSendWake, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp, wdfdevice/WdfDevStatePwrPolTimerExpiredWakeSucceeded, wdfdevice/WdfDevStatePwrPolWaitingArmed, wdfdevice/WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS, wdfdevice/WdfDevStatePwrPolWaitingArmedQueryIdle, wdfdevice/WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS, wdfdevice/WdfDevStatePwrPolWaitingArmedUsbSS, wdfdevice/WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS, wdfdevice/WdfDevStatePwrPolWaitingArmedWakeInterruptFired, wdfdevice/WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown, wdfdevice/WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS, wdfdevice/WdfDevStatePwrPolWaitingUnarmed, wdfdevice/WdfDevStatePwrPolWaitingUnarmedQueryIdle, wdfdevice/WdfDevStatePwrPolWakeCapableDeviceIdle, wdfdevice/WdfDevStatePwrPolWakeCapableUsbSSCompleted, wdfdevice/WdfDevStatePwrPolWakeFailedUsbSS, wdfdevice/WdfDevStatePwrPolWokeFromS0, wdfdevice/WdfDevStatePwrPolWokeFromS0NotifyDriver, wdfdevice/WdfDevStatePwrPolWokeFromS0UsbSS"
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfdevice.h
api_name:
-	WDF_DEVICE_POWER_POLICY_STATE
product: Windows
targetos: Windows
req.typenames: WDF_DEVICE_POWER_POLICY_STATE, *PWDF_DEVICE_POWER_POLICY_STATE
req.product: Windows 10 or later.
---

# _WDF_DEVICE_POWER_POLICY_STATE Enumeration
<p class="CCE_Message">[Applies to KMDF only]

The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter.

## Syntax
```
typedef enum _WDF_DEVICE_POWER_POLICY_STATE {
  WdfDevStatePwrPolInvalid                                                     ,
  WdfDevStatePwrPolObjectCreated                                               ,
  WdfDevStatePwrPolStarting                                                    ,
  WdfDevStatePwrPolStartingSucceeded                                           ,
  WdfDevStatePwrPolStartingFailed                                              ,
  WdfDevStatePwrPolStartingDecideS0Wake                                        ,
  WdfDevStatePwrPolStartedIdleCapable                                          ,
  WdfDevStatePwrPolTimerExpiredNoWake                                          ,
  WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown                         ,
  WdfDevStatePwrPolWaitingUnarmed                                              ,
  WdfDevStatePwrPolWaitingUnarmedQueryIdle                                     ,
  WdfDevStatePwrPolS0NoWakePowerUp                                             ,
  WdfDevStatePwrPolS0NoWakeCompletePowerUp                                     ,
  WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed                         ,
  WdfDevStatePwrPolSystemSleepNeedWake                                         ,
  WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp                          ,
  WdfDevStatePwrPolSystemSleepPowerRequestFailed                               ,
  WdfDevStatePwrPolCheckPowerPageable                                          ,
  WdfDevStatePwrPolSleepingWakeWakeArrived                                     ,
  WdfDevStatePwrPolSleepingWakeRevertArmWake                                   ,
  WdfDevStatePwrPolSystemAsleepWakeArmed                                       ,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabled                                 ,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled                     ,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisarm                                  ,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggered                               ,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0                             ,
  WdfDevStatePwrPolSystemWakeDeviceWokeDisarm                                  ,
  WdfDevStatePwrPolSleepingWakeWakeArrivedNP                                   ,
  WdfDevStatePwrPolSleepingWakeRevertArmWakeNP                                 ,
  WdfDevStatePwrPolSleepingWakePowerDownFailed                                 ,
  WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled                     ,
  WdfDevStatePwrPolSystemAsleepWakeArmedNP                                     ,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP                               ,
  WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP                   ,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP                                ,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP                             ,
  WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP                           ,
  WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP                                ,
  WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp                         ,
  WdfDevStatePwrPolSleeping                                                    ,
  WdfDevStatePwrPolSleepingNoWakePowerDown                                     ,
  WdfDevStatePwrPolSleepingNoWakeCompletePowerDown                             ,
  WdfDevStatePwrPolSleepingNoWakeDxRequestFailed                               ,
  WdfDevStatePwrPolSleepingWakePowerDown                                       ,
  WdfDevStatePwrPolSleepingSendWake                                            ,
  WdfDevStatePwrPolSystemAsleepNoWake                                          ,
  WdfDevStatePwrPolSystemWakeDeviceWakeDisabled                                ,
  WdfDevStatePwrPolSystemWakeDeviceToD0                                        ,
  WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp                         ,
  WdfDevStatePwrPolSystemWakeQueryIdle                                         ,
  WdfDevStatePwrPolStartedWakeCapable                                          ,
  WdfDevStatePwrPolTimerExpiredDecideUsbSS                                     ,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown                            ,
  WdfDevStatePwrPolTimerExpiredWakeCapableSendWake                             ,
  WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS                                ,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived                          ,
  WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake                           ,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled                         ,
  WdfDevStatePwrPolTimerExpiredWakeCapableCleanup                              ,
  WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed                        ,
  WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown                          ,
  WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp                            ,
  WdfDevStatePwrPolWaitingArmedUsbSS                                           ,
  WdfDevStatePwrPolWaitingArmed                                                ,
  WdfDevStatePwrPolWaitingArmedQueryIdle                                       ,
  WdfDevStatePwrPolIoPresentArmed                                              ,
  WdfDevStatePwrPolIoPresentArmedWakeCanceled                                  ,
  WdfDevStatePwrPolS0WakeDisarm                                                ,
  WdfDevStatePwrPolS0WakeCompletePowerUp                                       ,
  WdfDevStatePwrPolTimerExpiredWakeSucceeded                                   ,
  WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm                             ,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded                        ,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed                           ,
  WdfDevStatePwrPolWakeFailedUsbSS                                             ,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake            ,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled          ,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS                 ,
  WdfDevStatePwrPolCancelingWakeForSystemSleep                                 ,
  WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled                     ,
  WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp                  ,
  WdfDevStatePwrPolPowerUpForSystemSleepFailed                                 ,
  WdfDevStatePwrPolWokeFromS0UsbSS                                             ,
  WdfDevStatePwrPolWokeFromS0                                                  ,
  WdfDevStatePwrPolWokeFromS0NotifyDriver                                      ,
  WdfDevStatePwrPolStoppingResetDevice                                         ,
  WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp                          ,
  WdfDevStatePwrPolStoppingResetDeviceFailed                                   ,
  WdfDevStatePwrPolStoppingD0                                                  ,
  WdfDevStatePwrPolStoppingD0Failed                                            ,
  WdfDevStatePwrPolStoppingDisarmWake                                          ,
  WdfDevStatePwrPolStoppingDisarmWakeCancelWake                                ,
  WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled                              ,
  WdfDevStatePwrPolStopping                                                    ,
  WdfDevStatePwrPolStoppingFailed                                              ,
  WdfDevStatePwrPolStoppingSendStatus                                          ,
  WdfDevStatePwrPolStoppingCancelTimer                                         ,
  WdfDevStatePwrPolStoppingWaitForIdleTimeout                                  ,
  WdfDevStatePwrPolStoppingCancelUsbSS                                         ,
  WdfDevStatePwrPolStoppingWaitForUsbSSCompletion                              ,
  WdfDevStatePwrPolStoppingCancelWake                                          ,
  WdfDevStatePwrPolStopped                                                     ,
  WdfDevStatePwrPolCancelUsbSS                                                 ,
  WdfDevStatePwrPolStarted                                                     ,
  WdfDevStatePwrPolStartedCancelTimer                                          ,
  WdfDevStatePwrPolStartedWaitForIdleTimeout                                   ,
  WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep                       ,
  WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout                        ,
  WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS                             ,
  WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep                       ,
  WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout                        ,
  WdfDevStatePwrPolDeviceD0PowerRequestFailed                                  ,
  WdfDevStatePwrPolDevicePowerRequestFailed                                    ,
  WdfDevStatePwrPolGotoDx                                                      ,
  WdfDevStatePwrPolGotoDxInDx                                                  ,
  WdfDevStatePwrPolDx                                                          ,
  WdfDevStatePwrPolGotoD0                                                      ,
  WdfDevStatePwrPolGotoD0InD0                                                  ,
  WdfDevStatePwrPolFinal                                                       ,
  WdfDevStatePwrPolSleepingPowerDownNotProcessed                               ,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed                ,
  WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed                     ,
  WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer               ,
  WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown                         ,
  WdfDevStatePwrPolStoppingPoweringUp                                          ,
  WdfDevStatePwrPolStoppingPoweringDown                                        ,
  WdfDevStatePwrPolPowerUpForSystemSleepNotSeen                                ,
  WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS                             ,
  WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS                           ,
  WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS                            ,
  WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS                        ,
  WdfDevStatePwrPolCancelingUsbSSForSystemSleep                                ,
  WdfDevStatePwrPolStoppingD0CancelUsbSS                                       ,
  WdfDevStatePwrPolStartingPoweredUp                                           ,
  WdfDevStatePwrPolIdleCapableDeviceIdle                                       ,
  WdfDevStatePwrPolDeviceIdleReturnToActive                                    ,
  WdfDevStatePwrPolDeviceIdleSleeping                                          ,
  WdfDevStatePwrPolDeviceIdleStopping                                          ,
  WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown                             ,
  WdfDevStatePwrPolWakeCapableDeviceIdle                                       ,
  WdfDevStatePwrPolWakeCapableUsbSSCompleted                                   ,
  WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown                        ,
  WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted                    ,
  WdfDevStatePwrPolStoppedRemoving                                             ,
  WdfDevStatePwrPolRemoved                                                     ,
  WdfDevStatePwrPolRestarting                                                  ,
  WdfDevStatePwrPolRestartingFailed                                            ,
  WdfDevStatePwrPolStartingPoweredUpFailed                                     ,
  WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive                            ,
  WdfDevStatePwrPolWaitingArmedWakeInterruptFired                              ,
  WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired                          ,
  WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP                        ,
  WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived                 ,
  WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived  ,
  WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown               ,
  WdfDevStatePwrPolNull
} WDF_DEVICE_POWER_POLICY_STATE, *PWDF_DEVICE_POWER_POLICY_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>WdfDevStatePwrPolInvalid</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolObjectCreated</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStarting</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartingSucceeded</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartingFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartingDecideS0Wake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedIdleCapable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredNoWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingUnarmed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingUnarmedQueryIdle</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolS0NoWakePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolS0NoWakeCompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemSleepFromDeviceWaitingUnarmed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemSleepNeedWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemSleepNeedWakeCompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemSleepPowerRequestFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolCheckPowerPageable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakeWakeArrived</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakeRevertArmWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemAsleepWakeArmed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeEnabled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeDisarm</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeTriggered</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWokeDisarm</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakeWakeArrivedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakeRevertArmWakeNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakePowerDownFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakePowerDownFailedWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemAsleepWakeArmedNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeEnabledNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeEnabledWakeCanceledNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeDisarmNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeTriggeredS0NP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWokeDisarmNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeCompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleeping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingNoWakePowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingNoWakeCompletePowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingNoWakeDxRequestFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingWakePowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingSendWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemAsleepNoWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeDisabled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceToD0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceToD0CompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeQueryIdle</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedWakeCapable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredDecideUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableSendWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableWakeArrived</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableCancelWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableCleanup</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableDxAllocFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCompletedPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCompletedPowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedQueryIdle</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolIoPresentArmed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolIoPresentArmedWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolS0WakeDisarm</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolS0WakeCompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeSucceeded</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCompletedDisarm</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableWakeSucceeded</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableWakeFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWakeFailedUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedCancelWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolCancelingWakeForSystemSleep</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolCancelingWakeForSystemSleepWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDisarmingWakeForSystemSleepCompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolPowerUpForSystemSleepFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWokeFromS0UsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWokeFromS0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWokeFromS0NotifyDriver</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingResetDevice</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingResetDeviceCompletePowerUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingResetDeviceFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingD0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingD0Failed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingDisarmWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingDisarmWakeCancelWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingDisarmWakeWakeCanceled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStopping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingSendStatus</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingCancelTimer</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingWaitForIdleTimeout</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingCancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingWaitForUsbSSCompletion</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingCancelWake</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStopped</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolCancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedCancelTimer</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedWaitForIdleTimeout</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedWakeCapableCancelTimerForSleep</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedWakeCapableWaitForIdleTimeout</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedWakeCapableSleepingUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedIdleCapableCancelTimerForSleep</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartedIdleCapableWaitForIdleTimeout</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDeviceD0PowerRequestFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDevicePowerRequestFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolGotoDx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolGotoDxInDx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDx</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolGotoD0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolGotoD0InD0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolFinal</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSleepingPowerDownNotProcessed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownNotProcessed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredNoWakePowerDownNotProcessed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredNoWakePoweredDownDisableIdleTimer</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingWaitingForImplicitPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingPoweringUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingPoweringDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolPowerUpForSystemSleepNotSeen</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedStoppingCancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedWakeFailedCancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedIoPresentCancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedWakeSucceededCancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolCancelingUsbSSForSystemSleep</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppingD0CancelUsbSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartingPoweredUp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolIdleCapableDeviceIdle</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDeviceIdleReturnToActive</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDeviceIdleSleeping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolDeviceIdleStopping</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredNoWakeUndoPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWakeCapableDeviceIdle</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWakeCapableUsbSSCompleted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableUndoPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCompletedHardwareStarted</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStoppedRemoving</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolRemoved</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolRestarting</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolRestartingFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolStartingPoweredUpFailed</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredNoWakeReturnToActive</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedWakeInterruptFired</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFired</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolSystemWakeDeviceWakeInterruptFiredNP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapableWakeInterruptArrived</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolTimerExpiredWakeCapablePowerDownFailedWakeInterruptArrived</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolWaitingArmedWakeInterruptFiredDuringPowerDown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WdfDevStatePwrPolNull</td>
                    <td></td>
                </tr>
</table>

## Remarks

The WDF_DEVICE_POWER_POLICY_STATE enumeration is used as a member type in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551273">WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA</a> structure and as the return type for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545974">WdfDeviceGetDevicePowerPolicyState</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Header** | wdfdevice.h (include Wdf.h) |