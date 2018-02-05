---
UID : NE:pointofservicedriverinterface._PosPropertyId
title : "_PosPropertyId"
author : windows-driver-content
description : This enumeration defines the property identifiers for the properties that device drivers need to handle to be considered a barcode scanner or a magnetic strip reader (MSR).
old-location : pos\pospropertyid.htm
old-project : pos
ms.assetid : 82864db1-ee0a-4d41-a516-4e04befd2e89
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : PosPropertyId, pointofservicedriverinterface/MagneticStripeReaderCapabilities, MagneticStripeReaderCapabilities, pos.pospropertyid, pointofservicedriverinterface/MagneticStripeReaderIsDecodeDataEnabled, pointofservicedriverinterface/MagneticStripeReaderTracksToRead, MagneticStripeReaderIsDeviceAuthenticated, MagneticStripeReaderSupportedCardTypes, pointofservicedriverinterface/MagneticStripeReaderDataEncryptionAlgorithm, BarcodeScannerIsDecodeDataEnabled, pointofservicedriverinterface/IsEnabled, BarcodeScannerActiveProfile, pointofservicedriverinterface/MagneticStripeReaderIsDeviceAuthenticated, MagneticStripeReaderIsTransmitSentinelsEnabled, pointofservicedriverinterface/BarcodeScannerCapabilities, pointofservicedriverinterface/MagneticStripeReaderSupportedCardTypes, pointofservicedriverinterface/MagneticStripeReaderIsTransmitSentinelsEnabled, pointofservicedriverinterface/IsDisabledOnDataReceived, BarcodeScannerCapabilities, MagneticStripeReaderTracksToRead, BarcodeScannerActiveSymbologies, pointofservicedriverinterface/BarcodeScannerActiveProfile, MagneticStripeReaderDataEncryptionAlgorithm, MagneticStripeReaderErrorReportingType, pointofservicedriverinterface/BarcodeScannerSupportedProfiles, pointofservicedriverinterface/MagneticStripeReaderDeviceAuthenticationProtocol, pointofservicedriverinterface/MagneticStripeReaderErrorReportingType, BarcodeScannerSupportedProfiles, _PosPropertyId, pointofservicedriverinterface/PosPropertyId, pointofservicedriverinterface/BarcodeScannerActiveSymbologies, IsDisabledOnDataReceived, pointofservicedriverinterface/BarcodeScannerIsDecodeDataEnabled, MagneticStripeReaderDeviceAuthenticationProtocol, MagneticStripeReaderIsDecodeDataEnabled, BarcodeScannerSupportedSymbologies, IsEnabled, pointofservicedriverinterface/BarcodeScannerSupportedSymbologies, PosPropertyId enumeration
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pointofservicedriverinterface.h
req.include-header : Pointofservicedriverinterface.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Called at PASSIVE_LEVEL.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PosPropertyId
---

# _PosPropertyId Enumeration
This enumeration defines the property identifiers for the properties that device drivers need to handle to be considered a barcode scanner or a magnetic strip reader (MSR).

## Syntax
````
typedef enum _PosPropertyId { 
  IsEnabled                                         = 1,
  IsDisabledOnDataReceived                          = 4,
  BarcodeScannerIsDecodeDataEnabled                 = 5,
  BarcodeScannerCapabilities                        = 6,
  BarcodeScannerSupportedSymbologies                = 7,
  BarcodeScannerActiveSymbologies                   = 8,
  BarcodeScannerSupportedProfiles                   = 9,
  BarcodeScannerActiveProfile                       = 10,
  MagneticStripeReaderIsDecodeDataEnabled           = 11,
  MagneticStripeReaderCapabilities                  = 12,
  MagneticStripeReaderSupportedCardTypes            = 13,
  MagneticStripeReaderDeviceAuthenticationProtocol  = 14,
  MagneticStripeReaderErrorReportingType            = 15,
  MagneticStripeReaderTracksToRead                  = 16,
  MagneticStripeReaderIsTransmitSentinelsEnabled    = 17,
  MagneticStripeReaderIsDeviceAuthenticated         = 18,
  MagneticStripeReaderDataEncryptionAlgorithm       = 19
} PosPropertyId;
````

## Constants

<table>

<tr>
<td>BarcodeScannerActiveProfile</td>
<td>Sets the active device configuration profile. Configure the driver using one of the driver- or manufacturer-defined profiles in the list returned by the <b>BarcodeScannerSupportedProfiles</b> property. (Write-Only). For example, you may have one profile for warehouse staff and another profile for the sales department. Each profile is expected to configure the device based on the driver or manufacturer definition.</td>
</tr>

<tr>
<td>BarcodeScannerActiveSymbologies</td>
<td>Indicates the symbologies that the barcode scanner is actively handling. (Write-only). For symbology definitions, see <a href="..\pointofservicecommontypes\ne-pointofservicecommontypes-_barcodesymbology.md">BarcodeSymbology</a>.</td>
</tr>

<tr>
<td>BarcodeScannerCapabilities</td>
<td>Contains information about what functionality the barcode scanner supports. For example, a barcode scanner may support imaging and standard power reporting but not statistics updating and reporting. For more information about the values for barcode capabilities, see <a href="..\pointofservicedriverinterface\ns-pointofservicedriverinterface-_posbarcodescannercapabilitiestype.md">PosBarcodeScannerCapabilitiesType</a>. (Read-only).</td>
</tr>

<tr>
<td>BarcodeScannerIsDecodeDataEnabled</td>
<td>When set to <b>TRUE</b>, the driver must return decoded bar code data in the form of <b>ScanDataLabel</b> in addition to <b>ScanData</b> when raising a data received event. Decoded barcode data typically only contains data from the scanner with header information, scanner generated symbol character, and length identification removed. (Read/Write).</td>
</tr>

<tr>
<td>BarcodeScannerSupportedProfiles</td>
<td>Returns the list of supported driver-defined device configuration profiles. (Read-only).</td>
</tr>

<tr>
<td>BarcodeScannerSupportedSymbologies</td>
<td>Contains an array representing the complete list of symbologies that the barcode scanner is capable of reading. Also returns the number of bytes required for the array of symbologies. For symbology definitions, see <a href="..\pointofservicecommontypes\ne-pointofservicecommontypes-_barcodesymbology.md">BarcodeSymbology</a>. (Read-only).</td>
</tr>

<tr>
<td>BarcodeScannerVideoDeviceId</td>
<td></td>
</tr>

<tr>
<td>CashDrawerCapabilities</td>
<td></td>
</tr>

<tr>
<td>CashDrawerIsDrawerOpened</td>
<td></td>
</tr>

<tr>
<td>CashDrawerStatusProp</td>
<td></td>
</tr>

<tr>
<td>IsDisabledOnDataReceived</td>
<td>Indicates whether to disable the device after each scan event. This allows the hardware to enter an idle power-saving mode as frequently as possible. (Read/Write).</td>
</tr>

<tr>
<td>IsEnabled</td>
<td>Indicates whether the device is enabled. An enabled device is expected to be powered on and fully functional. In a disabled state, the device is not expected to generate input and can be powered down. (Read/Write).</td>
</tr>

<tr>
<td>LineDisplayBlinkRate</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCapabilities</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCharacterSet</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCharacterSetList</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCurrentWindow</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCursorAutoUpdateEnabled</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCursorPosition</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCursorTypeProperty</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCustomGlyphList</td>
<td></td>
</tr>

<tr>
<td>LineDisplayDeviceBrightness</td>
<td></td>
</tr>

<tr>
<td>LineDisplayDeviceControlDescription</td>
<td></td>
</tr>

<tr>
<td>LineDisplayDeviceControlVersion</td>
<td></td>
</tr>

<tr>
<td>LineDisplayDeviceServiceVersion</td>
<td></td>
</tr>

<tr>
<td>LineDisplayGlyphSizeInPixels</td>
<td></td>
</tr>

<tr>
<td>LineDisplayMapCharacterSet</td>
<td></td>
</tr>

<tr>
<td>LineDisplayMarqueeFormat</td>
<td></td>
</tr>

<tr>
<td>LineDisplayMarqueeRepeatWait</td>
<td></td>
</tr>

<tr>
<td>LineDisplayMarqueeType</td>
<td></td>
</tr>

<tr>
<td>LineDisplayMarqueeUnitWait</td>
<td></td>
</tr>

<tr>
<td>LineDisplayMaxBitmapSizeInPixels</td>
<td></td>
</tr>

<tr>
<td>LineDisplayPhysicalDeviceDescription</td>
<td></td>
</tr>

<tr>
<td>LineDisplayPhysicalDeviceName</td>
<td></td>
</tr>

<tr>
<td>LineDisplayScreenMode</td>
<td></td>
</tr>

<tr>
<td>LineDisplayScreenModeList</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowInterCharacterWaitInterval</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowSizeInCharacters</td>
<td></td>
</tr>

<tr>
<td>MagneticStripeReaderCapabilities</td>
<td>Returns a <a href="..\pointofservicedriverinterface\ns-pointofservicedriverinterface-_posmagneticstripereadercapabilitiestype.md">PosMagneticStripeReaderCapabilitiesType</a> that describes the capabilities of the MSR. (Read-Only).</td>
</tr>

<tr>
<td>MagneticStripeReaderDataEncryptionAlgorithm</td>
<td>Specifies the <a href="..\pointofservicedriverinterface\ne-pointofservicedriverinterface-_msrdataencryption.md">MsrDataEncryption</a> that will be used to encrypt the track data. (Read/write).</td>
</tr>

<tr>
<td>MagneticStripeReaderDeviceAuthenticationProtocol</td>
<td>The driver must return a <a href="https://msdn.microsoft.com/6f06d03e-001e-4340-9b96-8e3654be5c1a">MsrAuthenticationProtocolType</a> that describes the device authentication protocol supported by the MSR. (Read-only).</td>
</tr>

<tr>
<td>MagneticStripeReaderErrorReportingType</td>
<td>Specifies the level of error reporting that the MSR supports. For more information about the values for error reporting levels, see <a href="..\pointofservicedriverinterface\ne-pointofservicedriverinterface-_msrerrorreportingtype.md">MsrErrorReportingType</a>. (Read/write).</td>
</tr>

<tr>
<td>MagneticStripeReaderIsDecodeDataEnabled</td>
<td>Indicates whether to provide raw or decoded data from the most recently swiped card. If decoded data is provided to the application, set to <b>true</b>; otherwise, set to <b>false</b>. (Read/write).</td>
</tr>

<tr>
<td>MagneticStripeReaderIsDeviceAuthenticated</td>
<td>Indicates whether the device is authenticated. (Read-only).</td>
</tr>

<tr>
<td>MagneticStripeReaderIsTransmitSentinelsEnabled</td>
<td>Indicates whether the track data contains start and end sentinel values. (Read/write).</td>
</tr>

<tr>
<td>MagneticStripeReaderSupportedCardTypes</td>
<td>Returns an array of <a href="..\pointofservicedriverinterface\ne-pointofservicedriverinterface-_msrcardtype.md">MsrCardType</a>s supported by the MSR. (Read-only).</td>
</tr>

<tr>
<td>MagneticStripeReaderTracksToRead</td>
<td>Specifies which tracks the application will receive following a card swipe. Does not indicate the capability of the device hardware; instead, it is an application-configurable property representing the tracks to be read. For more information about track values, see <a href="..\pointofservicedriverinterface\ne-pointofservicedriverinterface-_msrtrackids.md">MsrTrackIds</a>. (Read/write).</td>
</tr>

<tr>
<td>PowerState</td>
<td></td>
</tr>

<tr>
<td>PrinterCapabilities</td>
<td></td>
</tr>

<tr>
<td>PrinterCartridgeNotifyEnabled</td>
<td></td>
</tr>

<tr>
<td>PrinterCharacterSet</td>
<td></td>
</tr>

<tr>
<td>PrinterCoverOpen</td>
<td></td>
</tr>

<tr>
<td>PrinterFlagWhenIdle</td>
<td></td>
</tr>

<tr>
<td>PrinterFontTypefaceList</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalCartridgeState</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalCurrentCartridge</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalLetterQuality</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalLineChars</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalLineHeight</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalLineSpacing</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalLineWidth</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalPaperEmpty</td>
<td></td>
</tr>

<tr>
<td>PrinterJournalPaperNearEnd</td>
<td></td>
</tr>

<tr>
<td>PrinterMapCharacterSet</td>
<td></td>
</tr>

<tr>
<td>PrinterMapMode</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModeArea</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModeDescriptor</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModeHorizontalPosition</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModePrintArea</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModePrintDirection</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModeStation</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModeVerticalPosition</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptCartridgeState</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptCurrentCartridge</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptLetterQuality</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptLineChars</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptLineHeight</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptLineSpacing</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptLinesToPaperCut</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptLineWidth</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptPaperEmpty</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptPaperNearEmpty</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptSidewaysMaxChars</td>
<td></td>
</tr>

<tr>
<td>PrinterReceiptSidewaysMaxLines</td>
<td></td>
</tr>

<tr>
<td>PrinterRotateSpecial</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipCartridgeState</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipCurrentCartridge</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipLetterQuality</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipLineChars</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipLineHeight</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipLinesNearEndToEnd</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipLineSpacing</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipLineWidth</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipMaxLines</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipPaperEmpty</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipPaperNearEmpty</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipPrintside</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipSideWaysMaxChars</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipSidewaysMaxLines</td>
<td></td>
</tr>

<tr>
<td>PrinterStatusProp</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedCharacterSets</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedJournalLineChars</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedReceiptBarcodeRotations</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedReceiptBitmapRotations</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedReceiptLineChars</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedSlipBarcodeRotations</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedSlipBitmapRotations</td>
<td></td>
</tr>

<tr>
<td>PrinterSupportedSlipLineChars</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |

## See Also

<a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_get_property.md">IOCTL_POINT_OF_SERVICE_GET_PROPERTY</a>

<a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_set_property.md">IOCTL_POINT_OF_SERVICE_SET_PROPERTY</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [pos\pos]:%20PosPropertyId enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>