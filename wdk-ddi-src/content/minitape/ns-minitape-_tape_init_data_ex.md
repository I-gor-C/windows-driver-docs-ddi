---
UID: NS.MINITAPE._TAPE_INIT_DATA_EX
title: _TAPE_INIT_DATA_EX
author: windows-driver-content
description: TAPE_INIT_DATA_EX defines values and routines that are specific to a Windows 2000 tape miniclass driver. The tape miniclass DriverEntry routine passes this information to the tape class driver to complete miniclass driver initialization.
old-location: storage\tape_init_data_ex.htm
old-project: storage
ms.assetid: 438c736e-c9be-4a75-a062-4614ea7fe028
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _TAPE_INIT_DATA_EX, TAPE_INIT_DATA_EX, *PTAPE_INIT_DATA_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_INIT_DATA_EX
req.alt-loc: minitape.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# _TAPE_INIT_DATA_EX structure



## -description
TAPE_INIT_DATA_EX defines values and routines that are specific to a Windows 2000 tape miniclass driver. The tape miniclass <b>DriverEntry</b> routine passes this information to the tape class driver to complete miniclass driver initialization. 



## -syntax

````
typedef struct _TAPE_INIT_DATA_EX {
  ULONG                        InitDataSize;
  TAPE_VERIFY_INQUIRY_ROUTINE  VerifyInquiry;
  BOOLEAN                      QueryModeCapabilitiesPage;
  ULONG                        MinitapeExtensionSize;
  TAPE_EXTENSION_INIT_ROUTINE  ExtensionInit;
  ULONG                        DefaultTimeOutValue;
  TAPE_ERROR_ROUTINE           TapeError;
  ULONG                        CommandExtensionSize;
  TAPE_PROCESS_COMMAND_ROUTINE CreatePartition;
  TAPE_PROCESS_COMMAND_ROUTINE Erase;
  TAPE_PROCESS_COMMAND_ROUTINE GetDriveParameters;
  TAPE_PROCESS_COMMAND_ROUTINE GetMediaParameters;
  TAPE_PROCESS_COMMAND_ROUTINE GetPosition;
  TAPE_PROCESS_COMMAND_ROUTINE GetStatus;
  TAPE_PROCESS_COMMAND_ROUTINE Prepare;
  TAPE_PROCESS_COMMAND_ROUTINE SetDriveParameters;
  TAPE_PROCESS_COMMAND_ROUTINE SetMediaParameters;
  TAPE_PROCESS_COMMAND_ROUTINE SetPosition;
  TAPE_PROCESS_COMMAND_ROUTINE WriteMarks;
  TAPE_PROCESS_COMMAND_ROUTINE PreProcessReadWrite;
  TAPE_PROCESS_COMMAND_ROUTINE TapeGetMediaTypes;
  ULONG                        MediaTypesSupported;
  TAPE_PROCESS_COMMAND_ROUTINE TapeWMIOperations;
  ULONG                        Reserved[2];
} TAPE_INIT_DATA_EX, *PTAPE_INIT_DATA_EX;
````


## -struct-fields

### -field InitDataSize

<dl>

### -field drivers can be as seamless as possible.


### -field VerifyInquiry

Specifies the entry point of the tape miniclass driver's <a href="storage.tapeminiverifyinquiry">TapeMiniVerifyInquiry</a> routine, which determines whether the driver supports a given device. This routine is required.


### -field QueryModeCapabilitiesPage

Directs the tape class driver when <b>TRUE</b> to pass a mode capabilities page to the tape miniclass driver's <a href="storage.tapeminiverifyinquiry">TapeMiniVerifyInquiry</a> and <a href="storage.tapeminiextensioninit">TapeMiniExtensionInit</a> routines.


### -field MinitapeExtensionSize

Specifies the size, in bytes, of a driver-specific context area. If this member is nonzero, <b>ExtensionInit </b>must not be <b>NULL</b>. This value is optional and must be set to zero if not used. 


### -field ExtensionInit

Pointer to the tape miniclass driver's <a href="storage.tapeminiextensioninit">TapeMiniExtensionInit</a> routine, which initializes an optional minitape extension, if any. If <b>MiniTapeExtensionSize</b> is zero, <b>ExtensionInit</b> must be <b>NULL</b>.


### -field DefaultTimeOutValue

Specifies the number of seconds that the tape class driver waits for an SRB request before canceling it. If this value is zero, the tape class driver sets an appropriate default value. The tape class driver always uses the default time-out value for read and write requests. The routines contained in the TAPE_INIT_DATA_EX structure can override the default time-out value for device control requests by setting <b>TimeOutValue</b> in an SRB.


### -field TapeError

Pointer to the tape miniclass driver's <a href="storage.tapeminitapeerror">TapeMiniTapeError</a> routine, which augments the error-handling activities of the tape class driver. This routine is optional. If one is not used, <b>TapeError</b> must be set to <b>NULL</b>.


### -field CommandExtensionSize

Specifies the size, in bytes, of a command extension to be allocated before the start of each tape command. A tape miniclass driver uses the command extension to store context during the processing of tape commands. Its size and internal structure are defined by the tape miniclass driver. A command extension is optional. If one is not used, <b>CommandExtensionSize</b> must be set to zero.


### -field CreatePartition

Pointer to the tape miniclass driver's <a href="storage.tapeminicreatepartition">TapeMiniCreatePartition</a> routine, which creates a partition on a tape. This routine is required.


### -field Erase

Pointer to the tape miniclass driver's <a href="storage.tapeminierase">TapeMiniErase</a> routine, which erases a tape. This routine is required.


### -field GetDriveParameters

Pointer to the tape miniclass driver's <a href="storage.tapeminigetdriveparameters">TapeMiniGetDriveParameters</a> routine, which handles requests to get drive parameters. This routine is required.


### -field GetMediaParameters

Pointer to the tape miniclass driver's <a href="storage.tapeminigetmediaparameters">TapeMiniGetMediaParameters</a> routine, which handles requests to get media parameters. This routine is required.


### -field GetPosition

Pointer to the tape miniclass driver's <a href="storage.tapeminigetposition">TapeMiniGetPosition</a> routine, which handles requests to get the position of a tape. This routine is required.


### -field GetStatus

Pointer to the tape miniclass driver's <a href="storage.tapeminigetstatus">TapeMiniGetStatus</a> routine, which handles requests for status. This routine is required.


### -field Prepare

Pointer to the tape miniclass driver's <a href="storage.tapeminiprepare">TapeMiniPrepare</a> routine, which prepares a tape device. This routine is required.


### -field SetDriveParameters

Pointer to the tape miniclass driver's <a href="storage.tapeminisetdriveparameters">TapeMiniSetDriveParameters</a> routine, which sets drive parameters. This routine is required.


### -field SetMediaParameters

Pointer to the tape miniclass driver's <a href="storage.tapeminisetmediaparameters">TapeMiniSetMediaParameters</a> routine, which sets media parameters. This routine is required.


### -field SetPosition

Pointer to the tape miniclass driver's <a href="storage.tapeminisetposition">TapeMiniSetPosition</a> routine, which positions a tape. This routine is required.


### -field WriteMarks

Pointer to the tape miniclass driver's <a href="storage.tapeminiwritemarks">TapeMiniWriteMarks</a> routine, which writes marks to tape. This routine is required.


### -field PreProcessReadWrite

Pointer to the tape miniclass driver's <a href="storage.tapeminipreprocessreadwrite">TapeMiniPreProcessReadWrite</a> routine, which executes device-specific operations before all reads and writes. This routine is optional and is not needed by most drivers. If one is not used, <b>PreProcessReadWrite</b> must be <b>NULL</b>.


### -field TapeGetMediaTypes

Pointer to the tape miniclass driver's <a href="storage.tapeminigetmediatypes">TapeMiniGetMediaTypes</a> routine, which gets a description of each media type supported by a tape device. This routine is required.


### -field MediaTypesSupported

Indicates the number of media types supported by the device.


### -field TapeWMIOperations

Pointer to the <a href="storage.tapeminiwmicontrol">TapeMiniWMIControl</a> routine. 


### -field Reserved

Reserved. 


## -remarks
A tape miniclass driver's <b>DriverEntry </b>routine calls <a href="storage.tapeclasszeromemory">TapeClassZeroMemory</a> to clear TAPE_INIT_DATA_EX, fills in the required members and any appropriate optional members, and <a href="storage.tapeclassinitialize">TapeClassInitialize</a> with a pointer to this structure.

The names of the tape miniclass driver routines indicated in the member descriptions of this structure are just placeholder names. The prototype for these routines is declared in <i>newtape.h</i> as follows:

The meaning of this prototype's parameters are different for each miniclass driver routine. For detailed information about how these parameters are used see the descriptions for each individual miniclass driver routine.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.driverentry_of_tape_miniclass_driver">DriverEntry of Tape Miniclass Driver</a>
</dt>
<dt>
<a href="storage.tapeclassinitialize">TapeClassInitialize</a>
</dt>
<dt>
<a href="storage.tapeclasszeromemory">TapeClassZeroMemory</a>
</dt>
<dt>
<a href="storage.tapeminicreatepartition">TapeMiniCreatePartition</a>
</dt>
<dt>
<a href="storage.tapeminierase">TapeMiniErase</a>
</dt>
<dt>
<a href="storage.tapeminiextensioninit">TapeMiniExtensionInit</a>
</dt>
<dt>
<a href="storage.tapeminigetdriveparameters">TapeMiniGetDriveParameters</a>
</dt>
<dt>
<a href="storage.tapeminigetmediaparameters">TapeMiniGetMediaParameters</a>
</dt>
<dt>
<a href="storage.tapeminigetmediatypes">TapeMiniGetMediaTypes</a>
</dt>
<dt>
<a href="storage.tapeminigetposition">TapeMiniGetPosition</a>
</dt>
<dt>
<a href="storage.tapeminigetstatus">TapeMiniGetStatus</a>
</dt>
<dt>
<a href="storage.tapeminiprepare">TapeMiniPrepare</a>
</dt>
<dt>
<a href="storage.tapeminisetdriveparameters">TapeMiniSetDriveParameters</a>
</dt>
<dt>
<a href="storage.tapeminisetmediaparameters">TapeMiniSetMediaParameters</a>
</dt>
<dt>
<a href="storage.tapeminisetposition">TapeMiniSetPosition</a>
</dt>
<dt>
<a href="storage.tapeminitapeerror">TapeMiniTapeError</a>
</dt>
<dt>
<a href="storage.tapeminiverifyinquiry">TapeMiniVerifyInquiry</a>
</dt>
<dt>
<a href="storage.tapeminiwritemarks">TapeMiniWriteMarks</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_INIT_DATA_EX structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

