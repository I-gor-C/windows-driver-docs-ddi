---
UID: NF.engextcpp.EXT_COMMAND
title: EXT_COMMAND
author: windows-driver-content
description: The EXT_COMMAND macro is used to define an extension command that was declared by using the EXT_COMMAND_METHOD macro.An extension command is defined as follows:
old-location: debugger\ext_command.htm
old-project: debugger
ms.assetid: 349712b1-bd1f-4f1f-a242-b6aa36e48773
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: EXT_COMMAND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EXT_COMMAND
req.alt-loc: engextcpp.hpp
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
req.iface: 
---

# EXT_COMMAND function



## -description
<p>The EXT_COMMAND macro is used to define an extension command that was declared by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544517">EXT_COMMAND_METHOD</a> macro.</p>
<p>An extension command is defined as follows:</p>


## -syntax

````
 EXT_COMMAND(
    _Name,
    _Desc,
    _Args
);
````


## -parameters
<dl>

### -param <i>_Name</i> 

<dd>
<p>The name of the extension command.  This must be the same as the <i>_Name</i> parameter that is used to declare the extension command by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff544517">EXT_COMMAND_METHOD</a>.</p>
<p>Because EXT_COMMAND is a macro, <i>_Name</i> must be the bare name of the extension command and should not be enclosed in quotation marks or be a variable.</p>
</dd>

### -param <i>_Desc</i> 

<dd>
<p>A string describing the extension command.</p>
</dd>

### -param <i>_Args</i> 

<dd>
<p>A string describing the arguments that are expected by the extension command.   For information about how the <i>_Args</i> string is formatted, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553340">Parsing Extension Arguments</a>.</p>
<div class="alert"><b>Note</b>     As an alternative to supplying a string that describes the arguments, you can use  the string "{{custom}}" to indicate that the extension command will parse the arguments itself.  The method <a href="https://msdn.microsoft.com/library/windows/hardware/ff548226">GetRawArgStr</a> can be used to fetch the raw argument for parsing.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The body of the extension command does not take any arguments.  However, because the extension command is declared as a method of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544508">EXT_CLASS</a> class, it has access to all the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543981">ExtExtension</a> base class, some of which are initialized for the execution of the extension command.</p>

<p>The macro <a href="https://msdn.microsoft.com/library/windows/hardware/ff544517">EXT_COMMAND_METHOD</a> should be used to declare the extension command.  As with all C++ declarations, the EXT_COMMAND_METHOD declaration should appear in the source files before the EXT_COMMAND definition.</p>

<p>When the debugger engine calls an extension command method, it wraps the call in a <b>try / except</b> block.  This protects the engine from some types of bugs in the extension code; but, since the extension calls are executed in the same thread as the engine, they can still cause it to crash.</p>

<p>This macro also creates a function called <i>_Name</i> (which calls the method defined by the macro).  In order for the engine to call the extension, this function must be exported from the extension library DLL.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff544508">EXT_CLASS</a> constant specifies the name of the C++ class that represents the EngExtCpp extension library.</p>

<p>EXT_CLASS</p>

<p>The default value of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544508">EXT_CLASS</a> is <b>Extension</b>.  You can change this value  by defining EXT_CLASS before you include the header file Engextcpp.hpp.</p>

<p>Each extension command in the library is declared as a member of the class EXT_CLASS using the macro <a href="https://msdn.microsoft.com/library/windows/hardware/ff544517">EXT_COMMAND_METHOD</a>.  For example, a library with two extension commands, <b>extcmd</b> and <b>anotherextcmd</b>, could define the class EXT_CLASS as follows:</p>

<p>Extension commands that have been declared by using EXT_COMMAND_METHOD should be defined by using <b>EXT_COMMAND</b> and should be exported from the library.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff544527">EXT_DECLARE_GLOBALS</a> macro creates a single instance of the EXT_CLASS class.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff544527">EXT_DECLARE_GLOBALS</a> macro sets up some global variables for use by the EngExtCpp extension framework.  This include creating a single instance of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544508">EXT_CLASS</a> class that represents the EngExtCpp extension library.</p>

<p>One of the source files to be compiled into the EngExtCpp extension library should include the following command</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544508">EXT_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544517">EXT_COMMAND_METHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543981">ExtExtension</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20EXT_COMMAND function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
