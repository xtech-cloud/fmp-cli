import os
from typing import Dict, List, Tuple
from generator.template.utility import writer

template = """
using Moq;
using Microsoft.Extensions.Options;
using XTC.FMP.MOD.File.App.Service;

public class YourMockDAO : YourDAO
{
    public YourMockDAO(IOptions<DatabaseSettings> _settings) : base(_settings)
    {
    }

    public YourMockDAO()
         : base(new DatabaseOptions())
    {

    }

    public static Mock<YourMockDAO> NewMock()
    {
        var mockDAO = new Mock<YourMockDAO>();
        mockDAO.Setup(
            m => m.CreateAsync(It.IsAny<YourEntity>())
        ).Returns(Task.CompletedTask);

        mockDAO.Setup(
          m => m.GetAsync(It.IsAny<string>())
        ).Returns(Task.FromResult(new YourEntity()));

        mockDAO.Setup(
           m => m.ListAsync(It.IsAny<int>(), It.IsAny<int>())
        ).Returns(Task.FromResult(new List<YourEntity>()));

        mockDAO.Setup(
            m => m.UpdateAsync(It.IsAny<string>(), It.IsAny<YourEntity>())
        ).Returns(Task.CompletedTask);

        mockDAO.Setup(
            m => m.RemoveAsync(It.IsAny<string>())
        ).Returns(Task.CompletedTask);
        return mockDAO;
    }
}

"""

def generate(
    _orgname: str,
    _modulename: str,
    _outputdir: str,
    _databasedriver
):
    if "mongodb" == _databasedriver:
        contents = template
        filepath = os.path.join(_outputdir, "MockDAO.cs")
        writer.write(filepath, contents, True)

